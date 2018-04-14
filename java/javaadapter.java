package adapter;

import java.util.Queue;
import java.util.LinkedList;

import java.io.InputStream;
import java.io.OutputStream;

import java.net.ServerSocket;
import java.net.Socket;

/************************************************************************************
//MAIN
 * 1.q synchronized
 * 2.C and JAVA  DataOutputStream,DataInputStream whitespace,NULL
 * 3.package java.net.SocketException
 * window
 * javac -g -d ./classes   -classpath  "classes/jar/emapij-72-8.4.3-RC1-07-01.jar;classes/jar/SET_EMAPI_2_7_1-04.jar;classes/jar/log4j-1.2.17.jar;classes/jar/log4j-api-2.0.jar;classes/jar/log4j-core-2.0.jar"  ./api/*.java
 * java -classpath  "jar/emapij-72-8.4.3-RC1-07-01.jar;jar/SET_EMAPI_2_7_1-04.jar;jar/log4j-1.2.17.jar;jar/log4j-api-2.0.jar;jar/log4j-core-2.0.jar"; api/JavaAdapter
 * linux 
 * javac -g -d ../bin -classpath "../lib/emapij-72-8.4.3-RC1-07-01.jar:../lib/SET_EMAPI_2_7_1-04.jar:../lib/log4j-1.2.17.jar:../lib/log4j-api-2.0.jar:../lib/log4j-core-2.0.jar" *.java 
 * java -classpath "../cfg/*:../lib/emapij-72-8.4.3-RC1-07-01.jar:../lib/SET_EMAPI_2_7_1-04.jar:../lib/log4j-1.2.17.jar:../lib/log4j-api-2.0.jar:../lib/log4j-core-2.0.jar": adapter/JavaAdapter  
************************************************************************************/
/*JavaAdapter*/
public class JavaAdapter {
   static Queue <String> q1 =new LinkedList<String>();      // FEED CP RD
   static Queue <String> q2 =new LinkedList<String>();      // FEED CP SD
   static Queue <String> q3 =new LinkedList<String>();      // FEED DP SD
   static Jcommon  cmm =new Jcommon();                      // 공통
   static String feedRD ="";
   static int    feedRDsize =0;
   static int    DPcnt =0;
   public static void main(String[] args) {
      cmm.ini();                                             //java.ini 셋팅
      cmm.setting();                                         //log4j2.xml 셋팅
      Thread t1 = new Thread(new CommandPort(cmm));          //CommandPort
      Thread t2 = new Thread(new DataPort   (cmm)); 		 //DataPort
      Thread t3 = new Thread(new CommandDiv  (q1,q2,q3,cmm));//EMAPI
      t1.start();
      t2.start();
      t3.start();
   }
}
/************************************************************************************
//CommandPort
 * 1.접속시도
 * 2.FEED 수신
 * 3.FEED 송신
 * 4.재접속시도(소켓끊길시)
************************************************************************************/
class CommandPort implements Runnable {
   ServerSocket  server   = null;
   Socket        socket   = null;
   OutputStream  os       = null;
   InputStream   is       = null;
   String        data     = null;
   String        cpdata   = null;
   String        sfalg    = "00";
   Jcommon       cmm      = null;
   Jlog          log      = new Jlog("cmdLogger");
   CommandPort(Jcommon  cmm){
      this.cmm =cmm;
   }
    public void run()  {
       try{
          log.log("CP Wait...");
          while(true){
             try{
                //1. 최초 접속 sfalg 00=접속시도,01=접속미시도
                if("00".equals(sfalg)){
                   server = new ServerSocket(20000);
                   socket = server.accept(); 
                   log.log("CP Connect");
                   sfalg="01";
                }
                //2. FEED --> CommandPort --> EMAPI
                is   = socket.getInputStream();
                cmm.receiveDataStream(is);
                //3. EMAPI --> CommandPort --> FEED
                synchronized (JavaAdapter.q2) {                           //Queue 동기화
                   while(!JavaAdapter.q2.isEmpty()){        
                      os  = socket.getOutputStream();
                      cpdata=cmm.sendDataStream(JavaAdapter.q2.peek(),os);//큐 복사 에러시 큐보존
                      log.log("CP     SD="+cpdata);                         
                      JavaAdapter.q2.poll();                              //큐 추출
                   }
                }
             //4. 재접속시도
             }catch(java.net.SocketException e){
                Thread.sleep(1000);
                //wait
                log.syslog(e);
                socket.close();
                log.log("CP Wait...");
                socket = server.accept();
                log.log("CP Connect");
                //retry
             }catch(Exception e){
                log.syslog(e);
                continue;
             }
          }
       }catch(Exception e){
          log.syslog(e);
       }
    }
}
/************************************************************************************
//DataPort
 *1. 접속시도
 *2. EMAPI --> DataPort --> FEED
 *3. 재접속시도 + 큐 처리    
************************************************************************************/
class DataPort implements Runnable{
   Socket socket;
   String         sfalg  = "00";
   OutputStream  os     = null;
   Jcommon       cmm    = null;
   String        dpdata = null;
   Jlog          dplog  = new Jlog("dataLogger");
   DataPort(Jcommon  cmm){
        this.cmm =cmm;
   }
    public void run() {
       try{
           while(true){
              try{
            	 //1. 접속시도 
                 if(sfalg.equals("00")){
                    socket= new Socket("127.0.0.1", 20001);
                    dplog.log("DP Connect");
                    sfalg="01";
                 }
                 //2. EMAPI --> DataPort --> FEED
                 synchronized (JavaAdapter.q3) {   //Queue 동기화
                    while(!JavaAdapter.q3.isEmpty()){
                       os     = socket.getOutputStream();
                       //큐 복사 에러시 큐보존
                       dpdata = cmm.sendDataStream((String)JavaAdapter.q3.peek() ,os);
                       JavaAdapter.DPcnt++;
                       dplog.log("DP     SD="+dpdata+"("+JavaAdapter.DPcnt+")");
                       //큐 추출
                       JavaAdapter.q3.poll();
                    }
                 }
              //3. 재접속시도 + 큐 처리    
              }catch(java.net.SocketException e){
                //wait
                 Thread.sleep(1000);
                 sfalg="00";
                 synchronized (JavaAdapter.q3) {
                    if(Boolean.valueOf(cmm.getQtimeOut())){
                       int time= cmm.getTime();
                       //연결해지  30초 초과시 큐 내용 비움 
                       if(time>3000){
                          JavaAdapter.q3.clear();
                          dplog.log("TimeDelay="+time);
                          dplog.log("Q Clear  ="+JavaAdapter.q3.size());
                          cmm.setReset();
                       }
                    }
                 }
                 continue;
              }catch(Exception e){
                 dplog.syslog(e);
              }
           }
       }catch(Exception e){
          dplog.syslog(e);
       }
    }
}

------------------------------------------------------------------------------------------------------------------
package adapter;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.SocketException;
import java.util.Properties;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import com.cinnober.proteus.emapi.EmapiMessage;
import com.cinnober.set.emapi.tagwire.EmapiSession;
import com.cinnober.proteus.emapi.EmapiMessageIf;

/************************************************************************************
//common
************************************************************************************/
public class Jcommon {
  Jlog                     log          = new Jlog("cmdLogger");
  String                   receivedata  = null;
  private Request          Request      = new Request ();
  private EmapiSession     emapiSession ;
  private String           timeflag     = "00";
  private DataInputStream  dis          = null;
  private DataOutputStream dos          = null;
  private String           qtimeout     = null;
  private Long             ftime        = null;
  private Long             ltime        = null;
  private String           cpport       = null;
  private String           dpport       = null;
  private String           logenvpath   = null;
  // code class
  final static String ERROR_RD       = "ERROR RD";
  final static String ERROR_SD       = "ERROR SD";
  final static String timeflag_00     = "00";
  final static String timeflag_01     = "01";
  //receivedata FEED로 부터 데이터 받는 함수
  public void receiveDataStream(InputStream is)   throws Exception{
      try{
         String rdbyte      = "";
         String bfdata[];
         String rdstr       = "";
         String receivedata = "";
         int    size=0;
         byte [] in    = new byte[1];
         dis=new DataInputStream(is);
         if(dis.available() !=0){                                               //패킷이용여부 처리 패킷이 없다면 Q2 실행 
            dis.readFully(in, 0, in.length);                                    //1byte 패킷받음
            rdbyte=new String (in, 0, in.length );								//1byte 패킷 문자로 추출
            JavaAdapter.feedRD+=rdbyte;
            if(JavaAdapter.feedRD.length()==6){                                 //길이정보 다 받았는지
              JavaAdapter.feedRDsize=Integer.parseInt(JavaAdapter.feedRD)+6;
            }
            //길이정보+문자정보를 다받고 사이즈가 0이 아닐때 완성된 문자열을 EMAPI호출 
            if(JavaAdapter.feedRD.length()==JavaAdapter.feedRDsize && JavaAdapter.feedRDsize !=0 ){
                synchronized (JavaAdapter.q1) { //Q1 동기화
                	log.log("CP     RD="+JavaAdapter.feedRD);	
                   JavaAdapter.q1.offer(JavaAdapter.feedRD);
                }
                //사용자 정의 커맨드 정의 부분 현재는 QUIT 하나 임의로 만들어둠 
                if("command".equals(JavaAdapter.feedRD.split(";")[1])){
                   command(JavaAdapter.feedRD.split(";")[2]);
                }
                //문자정보+길이정보 초기화
                JavaAdapter.feedRD="";
                JavaAdapter.feedRDsize  =0;
            }
         }
      }catch(java.io.EOFException a){
         log.syslog(a);
         throw new java.net.SocketException();
      }catch(Exception e){
         log.syslog(e);
      }
  }
  //send data  커맨드포트 혹은 데이터포트로 데이터 보내는 함수
  public String sendDataStream(String data,OutputStream os)  throws Exception {
      int len     = 0;
      String head = "";
      String rdata ="";
      try{
         dos = new DataOutputStream(os);
         if(data == null){
            len=0;
            data="000006;ERROR";
         }else{
            len=data.length()+1;
            head=String.format("%06d",len); //길이정보 생성
            data=head+";"+data;             //길이정보+;+문자정보
         }
         rdata=data;
         synchronized (dos) {
        	dos.writeBytes(data);              //byte화
        	//dos.flush();
		 }
         
      }catch(java.net.SocketException e){
         dis.close();
         log.syslog(e);
         throw new SocketException();
      }catch(Exception e){
         log.syslog(e);
         return ERROR_SD;
      }
      return rdata;
  }

