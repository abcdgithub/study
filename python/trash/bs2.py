import requests, BeautifulSoup
from bs4 import BeautifulSoup as bs4
import time



class market:
	ServiceKey=''
	def naversearch(self,dscd):
		r = requests.get('http://datalab.naver.com/keyword/realtimeList.naver?where=main')
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		article=soup.find("div",attrs={'class':"keyword_rank"})
		value =[]
		response =[]
		for content in article.findAll('li' ) :
			sno= content.find('em',attrs={'class':'num'}).text.encode('utf-8')
			title= content.find('span',attrs={'class':'title'}).text.encode('utf-8')
			key=['sno','title']
			value=[ sno,title]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			elif dscd == "B":
				value=[dao.sec(),sno,title]
				sql="insert into news0002 (base_dt,sno,title) values (:1,:2,:3)"
				rp=dao.insert(sql,value)
				response.append(rp)
			else:
				response.append(value)
		return response

	def kindkrxsearch(self,pageIndex,branchCode,kwd,fromData,toData,dscd):
		url='http://kind.krx.co.kr/news/rssnews.do?method=searchRssNews&fdName=all_news_idx&currentPageSize=15&pageIndex='+pageIndex+'&branchCode='+branchCode+'&kwd='+kwd+'&fromData='+fromData+'&toData='+toData
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).text
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item' ) :
			pubdate= content.find('pubdate').text.encode('utf-8')
			title= content.find('title').text.encode('utf-8')
			link= content.find('link').text.encode('utf-8')
			author= content.find('author').text.encode('utf-8')
			category= content.find('category').text.encode('utf-8')
			key=['pubdate','title','link','author','category']
			value=[pubdate, title,link,author,category]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response
	def kindkrxtoday(self,repIsuSrtCd,mktTpCd,searchCorpName,currentPageSize,dscd):
		url='http://kind.krx.co.kr/disclosure/rsstodaydistribute.do?method=searchRssTodayDistribute&repIsuSrtCd='+repIsuSrtCd+'&mktTpCd='+mktTpCd+'&searchCorpName='+searchCorpName+'&currentPageSize='+currentPageSize
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).text
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item' ) :
			title= content.find('title').text.encode('utf-8')
			link= content.find('link').text.encode('utf-8')
			pubdate= content.find('pubdate').text.encode('utf-8')
			author= content.find('author').text.encode('utf-8')
			category= content.find('category').text.encode('utf-8')
			language= content.find('language').text.encode('utf-8')
			lastbuilddate= content.find('lastbuilddate').text.encode('utf-8')
			key=['title','link','pubdate','author','category','language','lastbuilddate']
			value=[title, link,pubdate,author,category,language,lastbuilddate]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response
	def companysearch(self,crp_cd,dscd):
		if dscd == "Y" or dscd == "N" or dscd == "json":
			url='http://dart.fss.or.kr/api/company.xml?auth=556f4f974912afda8d3157dda56580be184a8cc4&crp_cd='+crp_cd
			fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
			r=requests.get(url, headers=fakeHeader)
			soup = BeautifulSoup.BeautifulSoup(r.content)
			r.close()
			result =[]
			response =[]
			for content in soup.findAll('result') :
				err_code= content.find('err_code').text.encode('utf-8')
				err_msg= content.find('err_msg').text.encode('utf-8')
				ercrp_nmr_code= content.find('crp_nm').text.encode('utf-8')
				crp_nm_e= content.find('crp_nm_e').text.encode('utf-8')
				crp_nm_i= content.find('crp_nm_i').text.encode('utf-8')
				stock_cd= content.find('stock_cd').text.encode('utf-8')
				ceo_nm= content.find('ceo_nm').text.encode('utf-8')
				crp_cls= content.find('crp_cls').text.encode('utf-8')
				crp_no= content.find('crp_no').text.encode('utf-8')
				bsn_no= content.find('bsn_no').text.encode('utf-8')
				adr= content.find('adr').text.encode('utf-8')
				hm_url= content.find('hm_url').text.encode('utf-8')
				ir_url= content.find('ir_url').text.encode('utf-8')
				phn_no= content.find('phn_no').text.encode('utf-8')
				fax_no= content.find('fax_no').text.encode('utf-8')
				ind_cd= content.find('ind_cd').text.encode('utf-8')
				est_dt= content.find('est_dt').text.encode('utf-8')
				acc_mt= content.find('acc_mt').text.encode('utf-8')
				key=['err_code','err_msg','ercrp_nmr_code','crp_nm_e','crp_nm_i','stock_cd','ceo_nm','crp_cls','crp_no','bsn_no','adr','hm_url','ir_url','phn_no','fax_no','ind_cd','est_dt','acc_mt']
				value=[err_code,err_msg,ercrp_nmr_code,crp_nm_e,crp_nm_i,stock_cd,ceo_nm,crp_cls,crp_no,bsn_no,adr,hm_url,ir_url,phn_no,fax_no,ind_cd,est_dt,acc_mt]


				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				else:
					response.append(value)
			return response


	def gongsisearch(self,crp_cd,end_dt,start_dt,fin_rpt,dsp_tp,bsn_tp,sort,series,page_no,page_set,dscd):
		if dscd == "Y" or dscd == "N"  or dscd == "json":
			url='http://dart.fss.or.kr/api/search.xml?auth=556f4f974912afda8d3157dda56580be184a8cc4&crp_cd='+crp_cd+'&end_dt='+end_dt+'&start_dt='+start_dt+'&fin_rpt='+fin_rpt+'&dsp_tp='+dsp_tp+'&bsn_tp='+bsn_tp+'&sort='+sort+'&series='+series+'&page_no='+page_no+'&page_set='+page_set
			fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
			r=requests.get(url, headers=fakeHeader)
			soup = BeautifulSoup.BeautifulSoup(r.content)
			r.close()
			result =[]
			response =[]
			for content in soup.findAll('list') :
				crp_cls= content.find('crp_cls').text.encode('utf-8')
				crp_nm= content.find('crp_nm').text.encode('utf-8')
				crp_cd= content.find('crp_cd').text.encode('utf-8')
				rpt_nm= content.find('rpt_nm').text.encode('utf-8')
				rcp_no= content.find('rcp_no').text.encode('utf-8')
				if dscd == "json":
					rcp_no='http://m.dart.fss.or.kr/html_mdart/MD1007.html?rcpNo='+rcp_no
				else:
					rcp_no='http://dart.fss.or.kr/dsaf001/main.do?rcpNo='+rcp_no

				flr_nm= content.find('flr_nm').text.encode('utf-8')
				rcp_dt= content.find('rcp_dt').text.encode('utf-8')
				rmk= content.find('rmk').text.encode('utf-8')
				key=['crp_cls','crp_nm','crp_cd','rpt_nm','rcp_no','flr_nm','rcp_dt','rmk']
				value=[crp_cls,crp_nm,crp_cd,rpt_nm,rcp_no,flr_nm,rcp_dt,rmk]

				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				else:
					response.append(value)
			return response

	def getFinancialTermMeaning(self,term,numOfRows,pageNo,dscd):
		url='http://api.seibro.or.kr/openapi/service/FnTermSvc/getFinancialTermMeaning?term='+term+'&numOfRows='+numOfRows+'&pageNo='+pageNo+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			fnceDictNm= content.find('fncedictnm').text.encode('utf-8')
			ksdfncedictdesccontent= content.find('ksdfncedictdesccontent').text.encode('utf-8')
			key=['fnceDictNm','ksdfncedictdesccontent']
			value=[fnceDictNm,ksdfncedictdesccontent]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response






	def getIssucoCustnoByNm(self,issucoNm,numOfRows,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoCustnoByNm?issucoNm='+issucoNm+'&numOfRows='+numOfRows+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			issucocustno= content.find('issucocustno').text.encode('utf-8')
			issuconm= content.find('issuconm').text.encode('utf-8')
			if content.find('listnm') != None :
				listnm= content.find('listnm').text.encode('utf-8')
			else:
				listnm=""
			key=['issucocustno','issuconm','listnm']
			value=[issucocustno,issuconm,listnm]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getStkIsinByNm(self,secnNm,numOfRows,pageNo,dscd):
		url='http://api.seibro.or.kr/openapi/service/StockSvc/getStkIsinByNm?secnNm='+secnNm+'&numOfRows='+numOfRows+'&pageNo='+pageNo+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			engsecnnm= content.find('engsecnnm').text.encode('utf-8')
			isin= content.find('isin').text.encode('utf-8')
			issudt= content.find('issudt').text.encode('utf-8')
			issucocustno= content.find('issucocustno').text.encode('utf-8')
			korsecnnm= content.find('korsecnnm').text.encode('utf-8')
			secnkacdnm= content.find('secnkacdnm').text.encode('utf-8')
			shotnisin= content.find('shotnisin').text.encode('utf-8')
			key=['engsecnnm','isin','issudt','issucocustno','korsecnnm','secnkacdnm','shotnisin']
			value=[engsecnnm,isin,issudt,issucocustno,korsecnnm,secnkacdnm,shotnisin]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response



	def getStkIsinByShortIsin(self,shortIsin,dscd):
		url='http://api.seibro.or.kr/openapi/service/StockSvc/getStkIsinByShortIsin?shortIsin='+shortIsin+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			engsecnnm= content.find('engsecnnm').text.encode('utf-8')
			isin= content.find('isin').text.encode('utf-8')
			issudt= content.find('issudt').text.encode('utf-8')
			issucocustno= content.find('issucocustno').text.encode('utf-8')
			korsecnnm= content.find('korsecnnm').text.encode('utf-8')
			secnkacdnm= content.find('secnkacdnm').text.encode('utf-8')
			shotnisin= content.find('shotnisin').text.encode('utf-8')
			key=['engsecnnm','isin','issudt','issucocustno','korsecnnm','secnkacdnm','shotnisin']
			value=[engsecnnm,isin,issudt,issucocustno,korsecnnm,secnkacdnm,shotnisin]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getDividendRank(self,year,rankTpcd,stkTpcd,listTpcd,dscd):
		url='http://api.seibro.or.kr/openapi/service/StockSvc/getDividendRank?year='+year+'&rankTpcd='+rankTpcd+'&stkTpcd='+stkTpcd+'&listTpcd='+listTpcd+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			caltotmarttpcd= content.find('caltotmarttpcd').text.encode('utf-8')
			divamtperstk= content.find('divamtperstk').text.encode('utf-8')
			divratecpri= content.find('divratecpri').text.encode('utf-8')
			divratepval= content.find('divratepval').text.encode('utf-8')
			issucocustno= content.find('issucocustno').text.encode('utf-8')
			korsecnnm= content.find('korsecnnm').text.encode('utf-8')
			num= content.find('num').text.encode('utf-8')
			pval= content.find('pval').text.encode('utf-8')
			secnkacd= content.find('secnkacd').text.encode('utf-8')
			setaccmm= content.find('setaccmm').text.encode('utf-8')
			setaccmmdd= content.find('setaccmmdd').text.encode('utf-8')
			shotnisin= content.find('shotnisin').text.encode('utf-8')
			key=['caltotmarttpcd','divamtperstk','divratecpri','divratepval','issucocustno','num','pval','secnkacd','setaccmm','setaccmmdd','shotnisin']
			value=[caltotmarttpcd,divamtperstk,divratecpri,divratepval,issucocustno,num,pval,secnkacd,setaccmm,setaccmmdd,shotnisin]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getSafeDpDutyDepoStatus(self,stdDt,listTpcd,dscd):
		url='http://api.seibro.or.kr/openapi/service/StockSvc/getSafeDpDutyDepoStatus?stdDt='+stdDt+'&listTpcd='+listTpcd+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			cocnt= content.find('cocnt').text.encode('utf-8')
			if content.find('issustkkindtpcd') != None :
				issustkkindtpcd= content.find('issustkkindtpcd').text.encode('utf-8')
			else:
				issustkkindtpcd=""

			issustkkindtpnm= content.find('issustkkindtpnm').text.encode('utf-8')
			issustkqty= content.find('issustkqty').text.encode('utf-8')
			safedpratiovalue= content.find('safedpratiovalue').text.encode('utf-8')
			secncnt= content.find('secncnt').text.encode('utf-8')
			stkdepoqty= content.find('stkdepoqty').text.encode('utf-8')
			key=  ['cocnt','issustkkindtpcd','issustkkindtpnm','issustkqty','safedpratiovalue','secncnt','stkdepoqty']
			value=   [cocnt,issustkkindtpcd,issustkkindtpnm,issustkqty,safedpratiovalue,secncnt,stkdepoqty]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def getSafeDpDutyDepoRgtStatus(self,stdDt,listTpcd,dscd):
		url='http://api.seibro.or.kr/openapi/service/StockSvc/getSafeDpDutyDepoRgtStatus?stdDt='+stdDt+'&listTpcd='+listTpcd+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			if content.find('codevaluenm') != None :
				codevaluenm= content.find('codevaluenm').text.encode('utf-8')
			else:
				codevaluenm=""
			if content.find('dutydeposecncnt') != None :
				dutydeposecncnt= content.find('dutydeposecncnt').text.encode('utf-8')
			else:
				dutydeposecncnt=""
			if content.find('dutydepococnt') != None :
				dutydepococnt= content.find('dutydepococnt').text.encode('utf-8')
			else:
				dutydepococnt=""
			if content.find('dutydepostkdepoqty') != None :
				dutydepostkdepoqty= content.find('dutydepostkdepoqty').text.encode('utf-8')
			else:
				dutydepostkdepoqty=""
			if content.find('safedpcocnt') != None :
				safedpcocnt= content.find('safedpcocnt').text.encode('utf-8')
			else:
				safedpcocnt=""
			if content.find('safedpracd') != None :
				safedpracd= content.find('safedpracd').text.encode('utf-8')
			else:
				safedpracd=""
			if content.find('safedpsecncnt') != None :
				safedpsecncnt= content.find('safedpsecncnt').text.encode('utf-8')
			else:
				safedpsecncnt=""
			if content.find('safedpstkdepoqty') != None :
				safedpstkdepoqty= content.find('safedpstkdepoqty').text.encode('utf-8')
			else:
				safedpstkdepoqty=""
			key=  ['codevaluenm','dutydepococnt','dutydeposecncnt','dutydepostkdepoqty','safedpcocnt','safedpracd','safedpsecncnt','safedpstkdepoqty']
			value=   [codevaluenm,dutydepococnt,dutydeposecncnt,dutydepostkdepoqty,safedpcocnt,safedpracd,safedpsecncnt,safedpstkdepoqty]


			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getNewDepoSecnList(self,yyyymm,searchType,issucoCustno,dscd):
		url='http://api.seibro.or.kr/openapi/service/StockSvc/getNewDepoSecnList?yyyymm='+yyyymm+'&searchType='+searchType+'&issucoCustno='+issucoCustno+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			aplidt= content.find('aplidt').text.encode('utf-8')
			indtpclsfno= content.find('indtpclsfno').text.encode('utf-8')
			indtpnm= content.find('indtpnm').text.encode('utf-8')
			isin= content.find('isin').text.encode('utf-8')
			issucocustno= content.find('issucocustno').text.encode('utf-8')
			korsecnnm= content.find('korsecnnm').text.encode('utf-8')
			pval= content.find('pval').text.encode('utf-8')
			secnkacd= content.find('secnkacd').text.encode('utf-8')
			secnkacdnm= content.find('secnkacdnm').text.encode('utf-8')
			setaccmm= content.find('setaccmm').text.encode('utf-8')
			totissuqty= content.find('totissuqty').text.encode('utf-8')
			key=  ['aplidt','indtpclsfno','indtpnm','isin','issucocustno','korsecnnm','pval','secnkacd','secnkacdnm','setaccmm','totissuqty']
			value=   [aplidt,indtpclsfno,indtpnm,isin,issucocustno,korsecnnm,pval,secnkacd,secnkacdnm,setaccmm,totissuqty]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def getStkDistributionRgtStdDt(self,issucoCustno,numOfRows,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getStkDistributionRgtStdDt?issucoCustno='+issucoCustno+'&numOfRows='+numOfRows+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			rgtstddt= content.find('rgtstddt').text.encode('utf-8')
			key=  ['rgtstddt']
			value=   [rgtstddt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getStkDistributionStatus(self,issucoCustno,rgtStdDt,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getStkDistributionStatus?issucoCustno='+issucoCustno+'&rgtStdDt='+rgtStdDt+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			shrs= content.find('shrs').text.encode('utf-8')
			shrsratio= content.find('shrsratio').text.encode('utf-8')
			stkdistbuttpnm= content.find('stkdistbuttpnm').text.encode('utf-8')
			stkqty= content.find('stkqty').text.encode('utf-8')
			stkqtyratio= content.find('stkqtyratio').text.encode('utf-8')
			key=  ['shrs','shrsratio','stkdistbuttpnm','stkqty','stkqtyratio']
			value=   [shrs,shrsratio,stkdistbuttpnm,stkqty,stkqtyratio]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getStkDistributionShareholderStatus(self,issucoCustno,rgtStdDt,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getStkDistributionShareholderStatus?issucoCustno='+issucoCustno+'&rgtStdDt='+rgtStdDt+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			shrs= content.find('shrs').text.encode('utf-8')
			shrsratio= content.find('shrsratio').text.encode('utf-8')
			stkdistbuttpnm= content.find('stkdistbuttpnm').text.encode('utf-8')
			stkqty= content.find('stkqty').text.encode('utf-8')
			stkqtyratio= content.find('stkqtyratio').text.encode('utf-8')
			key=  ['shrs','shrsratio','stkdistbuttpnm','stkqty','stkqtyratio']
			value=   [shrs,shrsratio,stkdistbuttpnm,stkqty,stkqtyratio]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getStkDistributionOwnQtyStatus(self,issucoCustno,rgtStdDt,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getStkDistributionOwnQtyStatus?issucoCustno='+issucoCustno+'&rgtStdDt='+rgtStdDt+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			shrs= content.find('shrs').text.encode('utf-8')
			shrsratio= content.find('shrsratio').text.encode('utf-8')
			stkdistbuttpnm= content.find('stkdistbuttpnm').text.encode('utf-8')
			stkqty= content.find('stkqty').text.encode('utf-8')
			key=  ['shrs','shrsratio','stkdistbuttpnm','stkqty']
			value=   [shrs,shrsratio,stkdistbuttpnm,stkqty]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getStkDistributionRegionStatus(self,issucoCustno,rgtStdDt,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getStkDistributionRegionStatus?issucoCustno='+issucoCustno+'&rgtStdDt='+rgtStdDt+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			shrs= content.find('shrs').text.encode('utf-8')
			shrsratio= content.find('shrsratio').text.encode('utf-8')
			stkdistbuttpnm= content.find('stkdistbuttpnm').text.encode('utf-8')
			stkqty= content.find('stkqty').text.encode('utf-8')
			key=  ['shrs','shrsratio','stkdistbuttpnm','stkqty']
			value=   [shrs,shrsratio,stkdistbuttpnm,stkqty]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response
	def getStkDistributionAgeStatus(self,issucoCustno,rgtStdDt,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getStkDistributionAgeStatus?issucoCustno='+issucoCustno+'&rgtStdDt='+rgtStdDt+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			shrs= content.find('shrs').text.encode('utf-8')
			shrsratio= content.find('shrsratio').text.encode('utf-8')
			stkdistbuttpnm= content.find('stkdistbuttpnm').text.encode('utf-8')
			stkqty= content.find('stkqty').text.encode('utf-8')
			key=  ['shrs','shrsratio','stkdistbuttpnm','stkqty']
			value=   [shrs,shrsratio,stkdistbuttpnm,stkqty]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getStkDistributionGenderStatus(self,issucoCustno,rgtStdDt,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getStkDistributionGenderStatus?issucoCustno='+issucoCustno+'&rgtStdDt='+rgtStdDt+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			shrs= content.find('shrs').text.encode('utf-8')
			shrsratio= content.find('shrsratio').text.encode('utf-8')
			stkdistbuttpnm= content.find('stkdistbuttpnm').text.encode('utf-8')
			stkqty= content.find('stkqty').text.encode('utf-8')
			key=  ['shrs','shrsratio','stkdistbuttpnm','stkqty']
			value=   [shrs,shrsratio,stkdistbuttpnm,stkqty]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getIssucoCustnoByShortIsin(self,shortIsin,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoCustnoByShortIsin?shortIsin='+shortIsin+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			issucocustno= content.find('issucocustno').text.encode('utf-8')
			issuconm= content.find('issuconm').text.encode('utf-8')
			listnm= content.find('listnm').text.encode('utf-8')

			key=  ['issucocustno','issuconm','listnm']
			value=   [issucocustno,issuconm,listnm]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def getSecnIssuInfoStock(self,issucoCustno,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getSecnIssuInfoStock?issucoCustno='+issucoCustno+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			caltotmarttpcd= content.find('caltotmarttpcd').text.encode('utf-8')
			isin= content.find('isin').text.encode('utf-8')
			korsecnnm= content.find('korsecnnm').text.encode('utf-8')
			shotnisin= content.find('shotnisin').text.encode('utf-8')
			stkkacd= content.find('stkkacd').text.encode('utf-8')
			totalstkcnt= content.find('totalstkcnt').text.encode('utf-8')
			key=  ['caltotmarttpcd','isin','korsecnnm','shotnisin','stkkacd','totalstkcnt']
			value=   [caltotmarttpcd,isin,korsecnnm,shotnisin,stkkacd,totalstkcnt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def getIssucoBasicInfo(self,issucoCustno,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoBasicInfo?issucoCustno='+issucoCustno+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			agorgtpcd= content.find('agorgtpcd').text.encode('utf-8')
			agorgtpcdnm= content.find('agorgtpcdnm').text.encode('utf-8')
			aplidt= content.find('aplidt').text.encode('utf-8')
			aplidty= content.find('aplidty').text.encode('utf-8')
			bizno= content.find('bizno').text.encode('utf-8')
			caltotmarttpcd= content.find('caltotmarttpcd').text.encode('utf-8')
			caltotmarttpcdnm= content.find('caltotmarttpcdnm').text.encode('utf-8')
			ceonm= content.find('ceonm').text.encode('utf-8')
			custxtindt= content.find('custxtindt').text.encode('utf-8')
			engcustnm= content.find('engcustnm').text.encode('utf-8')
			englegformnm= content.find('englegformnm').text.encode('utf-8')
			foundt= content.find('foundt').text.encode('utf-8')

			homepaddr= content.find('homepaddr').text.encode('utf-8')
			issucocustno= content.find('issucocustno').text.encode('utf-8')
			pval= content.find('pval').text.encode('utf-8')
			pvalstkqty= content.find('pvalstkqty').text.encode('utf-8')
			repsecnnm= content.find('repsecnnm').text.encode('utf-8')
			rostcloseterm= content.find('rostcloseterm').text.encode('utf-8')
			rostclosetermtpcd= content.find('rostclosetermtpcd').text.encode('utf-8')
			rostclosetermunitcd= content.find('rostclosetermunitcd').text.encode('utf-8')
			rostclosetermunitnm= content.find('rostclosetermunitnm').text.encode('utf-8')
			rostcloseterms= content.find('rostcloseterms').text.encode('utf-8')
			setaccmmdd= content.find('setaccmmdd').text.encode('utf-8')
			shotnisin= content.find('shotnisin').text.encode('utf-8')
			totalstkcnt= content.find('totalstkcnt').text.encode('utf-8')

			key=  ['agorgtpcd','agorgtpcdnm','aplidt','aplidty','bizno','caltotmarttpcd','caltotmarttpcdnm','ceonm','custxtindt','engcustnm','englegformnm','foundt','homepaddr','issucocustno','pval','pvalstkqty','repsecnnm','rostcloseterm','rostclosetermtpcd','rostclosetermunitcd','rostclosetermunitnm','rostcloseterms','setaccmmdd','shotnisin','totalstkcnt']
			value=   [agorgtpcd,agorgtpcdnm,aplidt,aplidty,bizno,caltotmarttpcd,caltotmarttpcdnm,ceonm,custxtindt,engcustnm,englegformnm,foundt,homepaddr,issucocustno,pval,pvalstkqty,repsecnnm,rostcloseterm,rostclosetermtpcd,rostclosetermunitcd,rostclosetermunitnm,rostcloseterms,setaccmmdd,shotnisin,totalstkcnt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def getIssucoStkQtyChgList(self,issucoCustno,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoStkQtyChgList?issucoCustno='+issucoCustno+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			issudt= content.find('issudt').text.encode('utf-8')
			issuqty= content.find('issuqty').text.encode('utf-8')
			secnissuracd= content.find('secnissuracd').text.encode('utf-8')
			secnissuracdnm= content.find('secnissuracdnm').text.encode('utf-8')
			key=  ['issudt','issuqty','secnissuracd','secnissuracdnm']
			value=   [issudt,issuqty,secnissuracd,secnissuracdnm]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def getIssucoPotentialStkQty(self,issucoCustno,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoPotentialStkQty?issucoCustno='+issucoCustno+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			issuremastkbw= content.find('issuremastkbw').text.encode('utf-8')
			issuremastkcb= content.find('issuremastkcb').text.encode('utf-8')
			key=  ['issuremastkbw','issuremastkcb']
			value=   [issuremastkbw,issuremastkcb]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getIssucoBondIssuStatus(self,issucoCustno,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoBondIssuStatus?issucoCustno='+issucoCustno+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			ectamt= content.find('ectamt').text.encode('utf-8')
			faceamt= content.find('faceamt').text.encode('utf-8')
			issukorremabw= content.find('issukorremabw').text.encode('utf-8')
			issukorremaeb= content.find('issukorremaeb').text.encode('utf-8')
			issukorremastk= content.find('issukorremastk').text.encode('utf-8')
			issurema= content.find('issurema').text.encode('utf-8')
			issucocustno= content.find('issucocustno').text.encode('utf-8')
			key=  ['ectamt','faceamt','issukorremabw','issukorremaeb','issukorremastk','issurema','issucocustno']
			value=   [ectamt,faceamt,issukorremabw,issukorremaeb,issukorremastk,issurema,issucocustno]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getIssucoRgtSchedule(self,issucoCustno,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoRgtSchedule?issucoCustno='+issucoCustno+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			repsecnnm= content.find('repsecnnm').text.encode('utf-8')
			rgtracd= content.find('rgtracd').text.encode('utf-8')
			rgtracdnm= content.find('rgtracdnm').text.encode('utf-8')
			rgtstddt= content.find('rgtstddt').text.encode('utf-8')
			key=  ['repsecnnm','rgtracd','rgtracdnm','rgtstddt']
			value=   [repsecnnm,rgtracd,rgtracdnm,rgtstddt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getCorpActionDtList(self,issucoCustno,listTpcd,dtTpcd,dscd):
		url='http://api.seibro.or.kr/openapi/service/CorpSvc/getCorpActionDtList?issucoCustno='+issucoCustno+'&listTpcd='+listTpcd+'&dtTpcd='+dtTpcd+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			repsecnnm= content.find('repsecnnm').text.encode('utf-8')
			rgtracd= content.find('rgtracd').text.encode('utf-8')
			rgtracdnm= content.find('rgtracdnm').text.encode('utf-8')
			rgtstddt= content.find('rgtstddt').text.encode('utf-8')
			key=  ['repsecnnm','rgtracd','rgtracdnm','rgtstddt']
			value=   [repsecnnm,rgtracd,rgtracdnm,rgtstddt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getSlbDealingByIsin(self,isin,dscd):
		url='http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbDealingByIsin?isin='+isin+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			matcqty= content.find('matcqty').text.encode('utf-8')
			redqty= content.find('redqty').text.encode('utf-8')
			slbtrremqty= content.find('slbtrremqty').text.encode('utf-8')
			stddt= content.find('stddt').text.encode('utf-8')
			key=  ['matcqty','redqty','slbtrremqty','stddt']
			value=   [matcqty,redqty,slbtrremqty,stddt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


##############################################################################################################################
	def getSlbStkTotalCostIndexList(self,fromDt,toDt,moveAvgTpcd,numOfRows,dscd):
		url='http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbStkTotalCostIndexList?fromDt='+fromDt+'&toDt='+toDt+'&moveAvgTpcd='+moveAvgTpcd+'&numOfRows='+numOfRows+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			daychng= content.find('daychng').text.encode('utf-8')
			slbindex= content.find('slbindex').text.encode('utf-8')
			stddt= content.find('stddt').text.encode('utf-8')
			key=  ['daychng','slbindex','stddt']
			value=   [daychng,slbindex,stddt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getSlbStkTotalBalanceIndexList(self,fromDt,toDt,numOfRows,dscd):
		url='http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbStkTotalBalanceIndexList?fromDt='+fromDt+'&toDt='+toDt+'&numOfRows='+numOfRows+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			daychng= content.find('daychng').text.encode('utf-8')
			slbindex= content.find('slbindex').text.encode('utf-8')
			stddt= content.find('stddt').text.encode('utf-8')
			key=  ['daychng','slbindex','stddt']
			value=   [daychng,slbindex,stddt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response
	def getSlbStkTop10CostIndexList(self,fromDt,toDt,moveAvgTpcd,numOfRows,dscd):
		url='http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbStkTop10CostIndexList?fromDt='+fromDt+'&toDt='+toDt+'&moveAvgTpcd='+moveAvgTpcd+'&numOfRows='+numOfRows+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :

			slbindex= content.find('slbindex').text.encode('utf-8')
			stddt= content.find('stddt').text.encode('utf-8')
			key=  ['slbindex','stddt']
			value=   [slbindex,stddt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getSlbStkTop10BalanceIndexList(self,fromDt,toDt,numOfRows,dscd):
		url='http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbStkTop10BalanceIndexList?fromDt='+fromDt+'&toDt='+toDt+'&numOfRows='+numOfRows+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :

			slbindex= content.find('slbindex').text.encode('utf-8')
			stddt= content.find('stddt').text.encode('utf-8')
			key=  ['slbindex','stddt']
			value=   [slbindex,stddt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def getSlbStkSpreadIndexList(self,fromDt,toDt,moveAvgTpcd,numOfRows,dscd):
		url='http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbStkSpreadIndexList?fromDt='+fromDt+'&toDt='+toDt+'&moveAvgTpcd='+moveAvgTpcd+'&numOfRows='+numOfRows+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :

			slbindex= content.find('slbindex').text.encode('utf-8')
			stddt= content.find('stddt').text.encode('utf-8')
			key=  ['slbindex','stddt']
			value=   [slbindex,stddt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def getSlbStkTop10SecnIndexList(self,stdDt,dscd):
		url='http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbStkTop10SecnIndexList?stdDt='+stdDt+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :

			balancerankisin= content.find('balancerankisin').text.encode('utf-8')
			balanceranksecnnm= content.find('balanceranksecnnm').text.encode('utf-8')
			costrankisin= content.find('costrankisin').text.encode('utf-8')
			costranksecnnm= content.find('costranksecnnm').text.encode('utf-8')
			indexbyrank= content.find('indexbyrank').text.encode('utf-8')
			stddt= content.find('stddt').text.encode('utf-8')
			key=  ['balancerankisin','balanceranksecnnm','costrankisin','costranksecnnm','indexbyrank','stddt']
			value=   [balancerankisin,balanceranksecnnm,costrankisin,costranksecnnm,indexbyrank,stddt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response



	def getSlbStkIndustrialCostIndexList(self,fromDt,toDt,moveAvgTpcd,numOfRows,dscd):
		url='http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbStkIndustrialCostIndexList?fromDt='+fromDt+'&toDt='+toDt+'&moveAvgTpcd='+moveAvgTpcd+'&numOfRows='+numOfRows+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			slbindex= content.find('slbindex').text.encode('utf-8')
			slbindexindtptpcd= content.find('slbindexindtptpcd').text.encode('utf-8')
			stddt= content.find('stddt').text.encode('utf-8')
			key=  ['slbindex','slbindexindtptpcd','stddt']
			value=   [slbindex,slbindexindtptpcd,stddt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response



	def getSlbStkIndustrialBalanceIndexList(self,fromDt,toDt,numOfRows,dscd):
		url='http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbStkIndustrialBalanceIndexList?fromDt='+fromDt+'&toDt='+toDt+'&numOfRows='+numOfRows+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :
			slbindex= content.find('slbindex').text.encode('utf-8')
			slbindexindtptpcd= content.find('slbindexindtptpcd').text.encode('utf-8')
			stddt= content.find('stddt').text.encode('utf-8')
			key=  ['slbindex','slbindexindtptpcd','stddt']
			value=   [slbindex,slbindexindtptpcd,stddt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def getSlbStkListedCostIndexList(self,fromDt,toDt,listTpcd,moveAvgTpcd,numOfRows,dscd):
		url='http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbStkListedCostIndexList?fromDt='+fromDt+'&toDt='+toDt+'&listTpcd='+listTpcd+'&moveAvgTpcd='+moveAvgTpcd+'&numOfRows='+numOfRows+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :

			slbindex= content.find('slbindex').text.encode('utf-8')
			stddt= content.find('stddt').text.encode('utf-8')
			key=  ['slbindex','stddt']
			value=   [slbindex,stddt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def getSlbStkListedBalanceIndexList(self,fromDt,toDt,listTpcd,numOfRows,dscd):
		url='http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbStkListedBalanceIndexList?fromDt='+fromDt+'&toDt='+toDt+'&listTpcd='+listTpcd+'&numOfRows='+numOfRows+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :

			slbindex= content.find('slbindex').text.encode('utf-8')
			stddt= content.find('stddt').text.encode('utf-8')
			key=  ['slbindex','stddt']
			value=   [slbindex,stddt]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response
		# http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbBondRank?stdDt=20140915&rankTpcd=1&ServiceKey=TXHf%2FXn4%2BL4q41bCxzAFSJ%2BP8oD8oXS51gFaRg0pORKpe18TmrvkhDyoFT%2FwvX3JeVG2sgysSYGHipENqfDjdQ%3D%3D
		# http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbStockRank?stdDt=20120305&rankTpcd=1&ServiceKey=TXHf%2FXn4%2BL4q41bCxzAFSJ%2BP8oD8oXS51gFaRg0pORKpe18TmrvkhDyoFT%2FwvX3JeVG2sgysSYGHipENqfDjdQ%3D%3D

	def getSlbStkIndexMarketRelationMatrix(self,stdDt,dscd):
		url='http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbStkIndexMarketRelationMatrix?stdDt='+stdDt+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :

			col1kospi= content.find('col1kospi').text.encode('utf-8')
			col2kospi200= content.find('col2kospi200').text.encode('utf-8')
			col3kosdaq100= content.find('col3kosdaq100').text.encode('utf-8')
			col4kospi200futures= content.find('col4kospi200futures').text.encode('utf-8')
			col5kospichg= content.find('col5kospichg').text.encode('utf-8')
			col6totalcostindex= content.find('col6totalcostindex').text.encode('utf-8')
			col7totalbalanceindex= content.find('col7totalbalanceindex').text.encode('utf-8')
			indexnm= content.find('indexnm').text.encode('utf-8')
			key=  ['col1kospi','col2kospi200','col3kosdaq100','col4kospi200futures','col5kospichg','col6totalcostindex','col7totalbalanceindex','indexnm']
			value=   [col1kospi,col2kospi200,col3kosdaq100,col4kospi200futures,col5kospichg,col6totalcostindex,col7totalbalanceindex,indexnm]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response



	def getElsDlsIsinByNm(self,secnNm,numOfRows,dscd):
		url='http://api.seibro.or.kr/openapi/service/DerivesSvc/getElsDlsIsinByNm?secnNm='+secnNm+'&numOfRows='+numOfRows+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :

			isin= content.find('isin').text.encode('utf-8')
			issucocustno= content.find('issucocustno').text.encode('utf-8')
			korsecnnm= content.find('korsecnnm').text.encode('utf-8')
			key=  ['isin','issucocustno','korsecnnm']
			value=   [isin,issucocustno,korsecnnm]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getElsDlsIssucoBalanceStatus(self,stdDt,dscd):
		url='http://api.seibro.or.kr/openapi/service/DerivesSvc/getElsDlsIssucoBalanceStatus?stdDt='+stdDt+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :

			balancesum= content.find('balancesum').text.encode('utf-8')
			dlsnsubsguarbalance= content.find('dlsnsubsguarbalance').text.encode('utf-8')
			dlsnsubsguarsecncnt= content.find('dlsnsubsguarsecncnt').text.encode('utf-8')
			dlsnsubsnguarbalance= content.find('dlsnsubsnguarbalance').text.encode('utf-8')
			dlsnsubsnguarsecncnt= content.find('dlsnsubsnguarsecncnt').text.encode('utf-8')
			dlssubsguarbalance= content.find('dlssubsguarbalance').text.encode('utf-8')
			dlssubsguarsecncnt= content.find('dlssubsguarsecncnt').text.encode('utf-8')
			dlssubsnguarbalance= content.find('dlssubsnguarbalance').text.encode('utf-8')
			dlssubsnguarsecncnt= content.find('dlssubsnguarsecncnt').text.encode('utf-8')
			elsnsubsguarbalance= content.find('elsnsubsguarbalance').text.encode('utf-8')
			elsnsubsguarsecncnt= content.find('elsnsubsguarsecncnt').text.encode('utf-8')
			elsnsubsnguarbalance= content.find('elsnsubsnguarbalance').text.encode('utf-8')
			elsnsubsnguarsecncnt= content.find('elsnsubsnguarsecncnt').text.encode('utf-8')
			elssubsguarbalance= content.find('elssubsguarbalance').text.encode('utf-8')
			elssubsguarsecncnt= content.find('elssubsguarsecncnt').text.encode('utf-8')
			elssubsnguarbalance= content.find('elssubsnguarbalance').text.encode('utf-8')
			elssubsnguarsecncnt= content.find('elssubsnguarsecncnt').text.encode('utf-8')
			repsecnnm= content.find('repsecnnm').text.encode('utf-8')
			secncntsum= content.find('secncntsum').text.encode('utf-8')
			key=  ['balancesum','dlsnsubsguarbalance','dlsnsubsguarsecncnt','dlsnsubsnguarbalance','dlsnsubsnguarsecncnt','dlssubsguarbalance','dlssubsguarsecncnt','dlssubsnguarbalance','dlssubsnguarsecncnt','elsnsubsguarbalance','elsnsubsguarsecncnt','elsnsubsnguarbalance','elsnsubsnguarsecncnt','elssubsguarbalance','elssubsguarsecncnt','elssubsnguarbalance','elssubsnguarsecncnt','repsecnnm','secncntsum']
			value=   [balancesum,dlsnsubsguarbalance,dlsnsubsguarsecncnt,dlsnsubsnguarbalance,dlsnsubsnguarsecncnt,dlssubsguarbalance,dlssubsguarsecncnt,dlssubsnguarbalance,dlssubsnguarsecncnt,elsnsubsguarbalance,elsnsubsguarsecncnt,elsnsubsnguarbalance,elsnsubsnguarsecncnt,elssubsguarbalance,elssubsguarsecncnt,elssubsnguarbalance,elssubsnguarsecncnt,repsecnnm,secncntsum]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response




	def getSlbBondRank(self,stdDt,rankTpcd,dscd):
		url='http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbBondRank?stdDt='+stdDt+'&rankTpcd='+rankTpcd+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll("item")[2:]:
			isin= content.find('isin').text.encode('utf-8')
			issurema= content.find('issurema').text.encode('utf-8')
			korsecnnm= content.find('korsecnnm').text.encode('utf-8')
			matcamt= content.find('matcamt').text.encode('utf-8')
			redamtval= content.find('redamtval').text.encode('utf-8')
			remamt= content.find('remamt').text.encode('utf-8')
			rnum= content.find('rnum').text.encode('utf-8')
			key=['isin','issurema','korsecnnm','matcamt','redamtval','remamt','rnum']
			value=[isin,issurema,korsecnnm,matcamt,redamtval,remamt,rnum]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getSlbStockRank(self,stdDt,rankTpcd,dscd):
		url='http://api.seibro.or.kr/openapi/service/SlbSvc/getSlbStockRank?stdDt='+stdDt+'&rankTpcd='+rankTpcd+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll("item")[2:]:

			isin= content.find('isin').text.encode('utf-8')
			korsecnnm= content.find('korsecnnm').text.encode('utf-8')
			matcqty= content.find('matcqty').text.encode('utf-8')
			recallredqty= content.find('recallredqty').text.encode('utf-8')
			redqty= content.find('redqty').text.encode('utf-8')
			remamt= content.find('remamt').text.encode('utf-8')
			shotnisin= content.find('shotnisin').text.encode('utf-8')
			slbtrremqty= content.find('slbtrremqty').text.encode('utf-8')
			key=['isin','korsecnnm','matcqty','recallredqty','redqty','remamt','shotnisin','slbtrremqty']
			value=[isin,korsecnnm,matcqty,recallredqty,redqty,remamt,shotnisin,slbtrremqty]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response




	def getMonthlyIssuRedStatus(self,yyyymm,bondYn,dscd):
		url='http://api.seibro.or.kr/openapi/service/DerivesSvc/getMonthlyIssuRedStatus?yyyymm='+yyyymm+'&bondYn='+bondYn+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :

			dlsearlyredkrwamt= content.find('dlsearlyredkrwamt').text.encode('utf-8')
			dlsearlyredkrwsecncnt= content.find('dlsearlyredkrwsecncnt').text.encode('utf-8')
			dlsearlyrednkrwamt= content.find('dlsearlyrednkrwamt').text.encode('utf-8')
			dlsearlyrednkrwsecncnt= content.find('dlsearlyrednkrwsecncnt').text.encode('utf-8')
			dlsissukrwamt= content.find('dlsissukrwamt').text.encode('utf-8')
			dlsissukrwsecncnt= content.find('dlsissukrwsecncnt').text.encode('utf-8')
			dlsissunkrwamt= content.find('dlsissunkrwamt').text.encode('utf-8')
			dlsissunkrwsecncnt= content.find('dlsissunkrwsecncnt').text.encode('utf-8')

			dlsredkrwamt= content.find('dlsredkrwamt').text.encode('utf-8')
			dlsredkrwsecncnt= content.find('dlsredkrwsecncnt').text.encode('utf-8')
			dlsrednkrwamt= content.find('dlsrednkrwamt').text.encode('utf-8')
			dlsrednkrwsecncnt= content.find('dlsrednkrwsecncnt').text.encode('utf-8')
			elsearlyredamt= content.find('elsearlyredamt').text.encode('utf-8')
			elsearlyredsecncnt= content.find('elsearlyredsecncnt').text.encode('utf-8')
			elsissuamt= content.find('elsissuamt').text.encode('utf-8')
			if content.find('elssubsnguarbalance') != None :
				elssubsnguarbalance= content.find('elssubsnguarbalance').text.encode('utf-8')
			else:
				elssubsnguarbalance=''
			if content.find('elssubsnguarsecncnt') != None :
				elssubsnguarsecncnt= content.find('elssubsnguarsecncnt').text.encode('utf-8')
			else:
				elssubsnguarsecncnt=''
			elsissusecncnt= content.find('elsissusecncnt').text.encode('utf-8')
			elsredamt= content.find('elsredamt').text.encode('utf-8')
			elsredsecncnt= content.find('elsredsecncnt').text.encode('utf-8')
			elwearlyredamt= content.find('elwearlyredamt').text.encode('utf-8')
			elwearlyredsecncnt= content.find('elwearlyredsecncnt').text.encode('utf-8')
			elwissuamt= content.find('elwissuamt').text.encode('utf-8')
			elwissusecncnt= content.find('elwissusecncnt').text.encode('utf-8')
			elwredamt= content.find('elwredamt').text.encode('utf-8')
			elwredsecncnt= content.find('elwredsecncnt').text.encode('utf-8')
			yyyymm= content.find('yyyymm').text.encode('utf-8')
			key=  ['dlsearlyredkrwamt','dlsearlyredkrwsecncnt','dlsearlyrednkrwamt','dlsearlyrednkrwsecncnt','dlsissukrwamt','dlsissukrwsecncnt','dlsissunkrwamt','dlsissunkrwsecncnt','dlsredkrwamt','dlsredkrwsecncnt','dlsrednkrwamt','dlsrednkrwsecncnt','elsearlyredamt','elsearlyredsecncnt','elsissuamt','elssubsnguarbalance','elssubsnguarsecncnt','elsissusecncnt','elsredamt','elsredsecncnt','elwearlyredamt','elwearlyredsecncnt','elwissuamt','elwissusecncnt','elwredamt','elwredsecncnt','yyyymm']
			value=   [dlsearlyredkrwamt,dlsearlyredkrwsecncnt,dlsearlyrednkrwamt,dlsearlyrednkrwsecncnt,dlsissukrwamt,dlsissukrwsecncnt,dlsissunkrwamt,dlsissunkrwsecncnt,dlsredkrwamt,dlsredkrwsecncnt,dlsrednkrwamt,dlsrednkrwsecncnt,elsearlyredamt,elsearlyredsecncnt,elsissuamt,elssubsnguarbalance,elssubsnguarsecncnt,elsissusecncnt,elsredamt,elsredsecncnt,elwearlyredamt,elwearlyredsecncnt,elwissuamt,elwissusecncnt,elwredamt,elwredsecncnt,yyyymm]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def getRecentRceptList(self,dscd):
		url='http://apis.data.go.kr/9710000/BillInfoService/getRecentRceptList?numOfRows=30&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :

			billid= content.find('billid').text.encode('utf-8')
			billname= content.find('billname').text.encode('utf-8')
			billno= content.find('billno').text.encode('utf-8')
			proposedt= content.find('proposedt').text.encode('utf-8')
			proposerkind= content.find('proposerkind').text.encode('utf-8')
			key=  ['billid','billname','billno','proposedt','proposerkind']
			value=   [billid,billname,billno,proposedt,proposerkind]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def selectWeekScheduleInfo(self,dscd):
		url='http://m.seibro.or.kr/cmuc/company/selectWeekScheduleInfo.do'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('tr')[1:]:
			base_dt=content.findAll('td')[0].text.encode('utf-8')
			en_nm=content.findAll('td')[1].text.encode('utf-8')
			resn=content.findAll('td')[2].text.encode('utf-8')
			mk_dscd=content.findAll('td')[3].text.encode('utf-8')
			key=['base_dt','en_nm','resn','mk_dscd']
			value=[base_dt,en_nm,resn,mk_dscd]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def selectDateSchedule(self,dscd):
		url='http://m.seibro.or.kr/cmuc/company/selectDateSchedule.do'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('tr')[1:]:
			en_nm=content.findAll('td')[0].text.encode('utf-8')
			base_dt=content.findAll('td')[1].text.encode('utf-8')
			mk_dscd=content.findAll('td')[2].text.encode('utf-8')
			resn=content.findAll('td')[3].text.encode('utf-8')
			key=['en_nm','base_dt','mk_dscd','resn']
			value=[en_nm,base_dt,mk_dscd,resn]
			print value
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getRecentPasageList(self,dscd):
		url='http://apis.data.go.kr/9710000/BillInfoService/getRecentPasageList?ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :

			billid= content.find('billid').text.encode('utf-8')
			billname= content.find('billname').text.encode('utf-8')
			billno= content.find('billno').text.encode('utf-8')
			committeename= content.find('committeename').text.encode('utf-8')
			generalresult= content.find('generalresult').text.encode('utf-8')
			procdt= content.find('procdt').text.encode('utf-8')
			proposedt= content.find('proposedt').text.encode('utf-8')
			proposerkind= content.find('proposerkind').text.encode('utf-8')
			key=  ['billid','billname','billno','committeename','generalresult','procdt','proposedt','proposerkind']
			value=   [billid,billname,billno,committeename,generalresult,procdt,proposedt,proposerkind]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def getBillReceiptInfo(self,bill_id,dscd):
		url='http://apis.data.go.kr/9710000/BillInfoService/getBillReceiptInfo?bill_id='+bill_id+'&ServiceKey='+self.ServiceKey
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('item') :

			billname= content.find('billname').text.encode('utf-8')
			billno= content.find('billno').text.encode('utf-8')
			if  content.find('bookhwpname') != None:
				bookhwpname= content.find('bookhwpname').text.encode('utf-8')
			else:
				bookhwpname=""
			if  content.find('bookhwpurl') != None:
				bookhwpurl= content.find('bookhwpurl').text.encode('utf-8')
			else:
				bookhwpurl=""
			if  content.find('bookpdfname') != None:
				bookpdfname= content.find('bookpdfname').text.encode('utf-8')
			else:
				bookpdfname=""
			if  content.find('bookpdfurl') != None:
				bookpdfurl= content.find('bookpdfurl').text.encode('utf-8')
			else:
				bookpdfurl=""
			proposedt= content.find('proposedt').text.encode('utf-8')
			proposeperiod= content.find('proposeperiod').text.encode('utf-8')
			proposer= content.find('proposer').text.encode('utf-8')
			summarylink= content.find('summarylink').text.encode('utf-8')
			key=  ['billname','billno','bookhwpname','bookhwpurl','bookpdfname','bookpdfurl','proposedt','proposeperiod','proposer','summarylink']
			value=   [billname,billno,bookhwpname,bookhwpurl,bookpdfname,bookpdfurl,proposedt,proposeperiod,proposer,summarylink]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def exchange(self,search_code,dscd):
		url='http://www.mibank.me/exchange/bank/index.php?search_code='+search_code
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll("tr")[2:]:

			nm=content.findAll('td')[2].text.encode('utf-8')
			cash_buy1=content.findAll('td')[3].text.encode('utf-8')
			cash_buy2=content.findAll('td')[4].text.encode('utf-8')
			cash_sell1=content.findAll('td')[5].text.encode('utf-8')
			cash_sell2=content.findAll('td')[6].text.encode('utf-8')
			cash_send1=content.findAll('td')[7].text.encode('utf-8')
			cash_send2=content.findAll('td')[8].text.encode('utf-8')
			txt_em=content.findAll('td')[9].text.encode('utf-8')
			key=['nm','cash_buy1','cash_buy2','cash_sell1','cash_sell2','cash_send1','cash_send2','txt_em']
			value=[nm,cash_buy1,cash_buy2,cash_sell1,cash_sell2,cash_send1,cash_send2,txt_em]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def dailystock(self,code,dscd):
		url='http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code='+code
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('dailystock') :
			day_date= content.get('day_date')
			day_endprice= content.get('day_endprice')
			day_dungrak= content.get('day_dungrak')
			day_getdebi= content.get('day_getdebi')
			day_start= content.get('day_start')
			day_high= content.get('day_high')
			day_low= content.get('day_low')
			day_volume= content.get('day_volume')
			day_getamount= content.get('day_getamount')
			key =['day_date','day_endprice','day_dungrak','day_getdebi','day_start','day_high','day_low','day_volume','day_getamount']
			value=[day_date,day_endprice,day_dungrak,day_getdebi,day_start,day_high,day_low,day_volume,day_getamount]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response
	def askprice(self,code,dscd):
		url='http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code='+code
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('askprice') :
			member_memdomem= content.get('member_memdomem')
			member_memdovol= content.get('member_memdovol')
			member_memsomem= content.get('member_memsomem')
			member_mesuovol= content.get('member_mesuovol')
			key =['member_memdomem','member_memdovol','member_memsomem','member_mesuovol']
			value=[member_memdomem,member_memdovol,member_memsomem,member_mesuovol]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response
	def tbl_stockinfo(self,code,dscd):
		url='http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code='+code
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('tbl_stockinfo') :
			jongname= content.get('jongname')
			curjuka= content.get('curjuka')
			dungrak= content.get('dungrak')
			debi= content.get('debi')
			prevjuka= content.get('prevjuka')
			volume= content.get('volume')
			money= content.get('money')
			startjuka= content.get('startjuka')
			highjuka= content.get('highjuka')
			lowjuka= content.get('lowjuka')
			high52= content.get('high52')
			low52= content.get('low52')
			upjuka= content.get('upjuka')
			downjuka= content.get('downjuka')
			per= content.get('per')
			amount= content.get('amount')
			facejuka= content.get('facejuka')
			key =['jongname','curjuka','dungrak','debi','prevjuka','volume','money','startjuka','highjuka','lowjuka','high52','low52','upjuka','downjuka','per','amount','facejuka']
			value=[jongname,curjuka,dungrak,debi,prevjuka,volume,money,startjuka,highjuka,lowjuka,high52,low52,upjuka,downjuka,per,amount,facejuka]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response
	def tbl_hoga(self,code,dscd):
		url='http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code='+code
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('tbl_hoga') :
			mesujan0= content.get('mesujan0')
			mesuhoka0= content.get('mesuhoka0')
			mesujan1= content.get('mesujan1')
			mesuhoka1= content.get('mesuhoka1')
			mesujan2= content.get('mesujan2')
			mesuhoka2= content.get('mesuhoka2')
			mesujan3= content.get('mesujan3')
			mesuhoka3= content.get('mesuhoka3')
			mesujan4= content.get('mesujan4')
			mesuhoka4= content.get('mesuhoka4')
			medojan0= content.get('medojan0')
			medohoka0= content.get('medohoka0')
			medojan1= content.get('medojan1')
			downjuka= content.get('downjuka')
			medohoka1= content.get('medohoka1')
			medojan2= content.get('medojan2')
			medohoka2= content.get('medohoka2')
			medojan3= content.get('medojan3')
			medohoka3= content.get('medohoka3')
			medojan4= content.get('medojan4')
			medohoka4= content.get('medohoka4')
			key =['mesujan0','mesuhoka0','mesujan1','mesuhoka1','mesujan2','mesuhoka2','mesujan3','mesuhoka3','mesujan4','mesuhoka4','medojan0','medohoka0','medojan1','downjuka','medohoka1','medojan2','medohoka2','medojan3','medohoka3','medojan4','medohoka4']
			value=[mesujan0,mesuhoka0,mesujan1,mesuhoka1,mesujan2,mesuhoka2,mesujan3,mesuhoka3,mesujan4,mesuhoka4,medojan0,medohoka0,medojan1,downjuka,medohoka1,medojan2,medohoka2,medojan3,medohoka3,medojan4,medohoka4]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response
	def tbl_timeconclude(self,code,dscd):
		url='http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code='+code
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('tbl_timeconclude') :
			time= content.get('time')
			negoprice= content.get('negoprice')
			dungrak= content.get('dungrak')
			debi= content.get('debi')
			sellprice= content.get('sellprice')
			buyprice= content.get('buyprice')
			amount= content.get('amount')
			key =['time','negoprice','dungrak','debi','sellprice','buyprice','amount']
			value=[time,negoprice,dungrak,debi,sellprice,buyprice,amount]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response
	def stockinfo(self,code,dscd):
		url='http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code='+code
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('stockinfo') :
			kosdaqjisu= content.get('kosdaqjisu')
			kosdaqjisubuho= content.get('kosdaqjisubuho')
			kosdaqjisudebi= content.get('kosdaqjisudebi')
			starjisu= content.get('starjisu')
			starjisubuho= content.get('starjisubuho')
			starjisudebi= content.get('starjisudebi')
			jisu50= content.get('jisu50')
			jisu50buho= content.get('jisu50buho')
			jisu50debi= content.get('jisu50debi')
			mynowtime= content.get('mynowtime')
			myjanggubun= content.get('myjanggubun')
			mypublicprice= content.get('mypublicprice')
			krx100jisu= content.get('krx100jisu')
			krx100buho= content.get('krx100buho')
			krx100debi= content.get('krx100debi')
			kospijisu= content.get('kospijisu')
			kospibuho= content.get('kospibuho')
			kospidebi= content.get('kospidebi')
			kospi200jisu= content.get('kospi200jisu')
			kospi200buho= content.get('kospi200buho')
			kospi200debi= content.get('kospi200debi')
			key =['kosdaqjisu','kosdaqjisubuho','kosdaqjisudebi','starjisu','starjisubuho','starjisudebi','jisu50','jisu50buho','jisu50debi','mynowtime','myjanggubun','mypublicprice','krx100jisu','krx100buho','krx100debi','kospijisu','kospibuho','kospidebi','kospi200jisu','kospi200buho','kospi200debi']
			value=[kosdaqjisu,kosdaqjisubuho,kosdaqjisudebi,starjisu,starjisubuho,starjisudebi,jisu50,jisu50buho,jisu50debi,mynowtime,myjanggubun,mypublicprice,krx100jisu,krx100buho,krx100debi,kospijisu,kospibuho,kospidebi,kospi200jisu,kospi200buho,kospi200debi]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response
	def krx_sise(self,code,dscd):
		url='http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code='+code
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('dailystock') :
			day_date= content.get('day_date')
			day_endprice= content.get('day_endprice')
			day_dungrak= content.get('day_dungrak')
			day_getdebi= content.get('day_getdebi')
			day_start= content.get('day_start')
			day_high= content.get('day_high')
			day_low= content.get('day_low')
			day_volume= content.get('day_volume')
			day_getamount= content.get('day_getamount')
			key =['day_date','day_endprice','day_dungrak','day_getdebi','day_start','day_high','day_low','day_volume','day_getamount']
			value=[day_date,day_endprice,day_dungrak,day_getdebi,day_start,day_high,day_low,day_volume,day_getamount]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		for content in soup.findAll('askprice') :
			member_memdomem= content.get('member_memdomem')
			member_memdovol= content.get('member_memdovol')
			member_memsomem= content.get('member_memsomem')
			member_mesuovol= content.get('member_mesuovol')
			key =['member_memdomem','member_memdovol','member_memsomem','member_mesuovol']
			value=[member_memdomem,member_memdovol,member_memsomem,member_mesuovol]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		for content in soup.findAll('tbl_stockinfo') :
			jongname= content.get('jongname')
			curjuka= content.get('curjuka')
			dungrak= content.get('dungrak')
			debi= content.get('debi')
			prevjuka= content.get('prevjuka')
			volume= content.get('volume')
			money= content.get('money')
			startjuka= content.get('startjuka')
			highjuka= content.get('highjuka')
			lowjuka= content.get('lowjuka')
			high52= content.get('high52')
			low52= content.get('low52')
			upjuka= content.get('upjuka')
			downjuka= content.get('downjuka')
			per= content.get('per')
			amount= content.get('amount')
			facejuka= content.get('facejuka')
			key =['jongname','curjuka','dungrak','debi','prevjuka','volume','money','startjuka','highjuka','lowjuka','high52','low52','upjuka','downjuka','per','amount','facejuka']
			value=[jongname,curjuka,dungrak,debi,prevjuka,volume,money,startjuka,highjuka,lowjuka,high52,low52,upjuka,downjuka,per,amount,facejuka]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		for content in soup.findAll('tbl_hoga') :
			mesujan0= content.get('mesujan0')
			mesuhoka0= content.get('mesuhoka0')
			mesujan1= content.get('mesujan1')
			mesuhoka1= content.get('mesuhoka1')
			mesujan2= content.get('mesujan2')
			mesuhoka2= content.get('mesuhoka2')
			mesujan3= content.get('mesujan3')
			mesuhoka3= content.get('mesuhoka3')
			mesujan4= content.get('mesujan4')
			mesuhoka4= content.get('mesuhoka4')
			medojan0= content.get('medojan0')
			medohoka0= content.get('medohoka0')
			medojan1= content.get('medojan1')
			downjuka= content.get('downjuka')
			medohoka1= content.get('medohoka1')
			medojan2= content.get('medojan2')
			medohoka2= content.get('medohoka2')
			medojan3= content.get('medojan3')
			medohoka3= content.get('medohoka3')
			medojan4= content.get('medojan4')
			medohoka4= content.get('medohoka4')
			key =['mesujan0','mesuhoka0','mesujan1','mesuhoka1','mesujan2','mesuhoka2','mesujan3','mesuhoka3','mesujan4','mesuhoka4','medojan0','medohoka0','medojan1','downjuka','medohoka1','medojan2','medohoka2','medojan3','medohoka3','medojan4','medohoka4']
			value=[mesujan0,mesuhoka0,mesujan1,mesuhoka1,mesujan2,mesuhoka2,mesujan3,mesuhoka3,mesujan4,mesuhoka4,medojan0,medohoka0,medojan1,downjuka,medohoka1,medojan2,medohoka2,medojan3,medohoka3,medojan4,medohoka4]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		for content in soup.findAll('tbl_timeconclude') :
			time= content.get('time')
			negoprice= content.get('negoprice')
			dungrak= content.get('dungrak')
			debi= content.get('debi')
			sellprice= content.get('sellprice')
			buyprice= content.get('buyprice')
			amount= content.get('amount')
			key =['time','negoprice','dungrak','debi','sellprice','buyprice','amount']
			value=[time,negoprice,dungrak,debi,sellprice,buyprice,amount]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)


		for content in soup.findAll('stockinfo') :
			kosdaqjisu= content.get('kosdaqjisu')
			kosdaqjisubuho= content.get('kosdaqjisubuho')
			kosdaqjisudebi= content.get('kosdaqjisudebi')
			starjisu= content.get('starjisu')
			starjisubuho= content.get('starjisubuho')
			starjisudebi= content.get('starjisudebi')
			jisu50= content.get('jisu50')
			jisu50buho= content.get('jisu50buho')
			jisu50debi= content.get('jisu50debi')
			mynowtime= content.get('mynowtime')
			myjanggubun= content.get('myjanggubun')
			mypublicprice= content.get('mypublicprice')
			krx100jisu= content.get('krx100jisu')
			krx100buho= content.get('krx100buho')
			krx100debi= content.get('krx100debi')
			kospijisu= content.get('kospijisu')
			kospibuho= content.get('kospibuho')
			kospidebi= content.get('kospidebi')
			kospi200jisu= content.get('kospi200jisu')
			kospi200buho= content.get('kospi200buho')
			kospi200debi= content.get('kospi200debi')
			key =['kosdaqjisu','kosdaqjisubuho','kosdaqjisudebi','starjisu','starjisubuho','starjisudebi','jisu50','jisu50buho','jisu50debi','mynowtime','myjanggubun','mypublicprice','krx100jisu','krx100buho','krx100debi','kospijisu','kospibuho','kospidebi','kospi200jisu','kospi200buho','kospi200debi']
			value=[kosdaqjisu,kosdaqjisubuho,kosdaqjisudebi,starjisu,starjisubuho,starjisudebi,jisu50,jisu50buho,jisu50debi,mynowtime,myjanggubun,mypublicprice,krx100jisu,krx100buho,krx100debi,kospijisu,kospibuho,kospidebi,kospi200jisu,kospi200buho,kospi200debi]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response



	def tbl_daecha_data(self,code,dscd):
		url='http://asp1.krx.co.kr/servlet/krx.asp.XMLJemu?code='+code
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		i=-1;

		for content in soup.findAll('tbl_daecha_data') :
			i=i+1

			hangmok0= content.get('hangmok'+str(i))
			year1money0= content.get('year1money'+str(i))
			year1gusungrate0= content.get('year1gusungrate'+str(i))
			year1junggamrate0= content.get('year1junggamrate'+str(i))
			year2money0= content.get('year2money'+str(i))
			year2gusungrate0= content.get('year2gusungrate'+str(i))
			year2junggamrate0= content.get('year2junggamrate'+str(i))
			year3money0= content.get('year3money'+str(i))
			year3gusungrate0= content.get('year3gusungrate'+str(i))
			year3junggamrate0= content.get('year3junggamrate'+str(i))
			key =['hangmok0','year1money0','year1gusungrate0','year1junggamrate0','year2money0','year2gusungrate0','year2junggamrate0','year3money0','year3gusungrate0','year3junggamrate0']
			value=[hangmok0,year1money0,year1gusungrate0,year1junggamrate0,year2money0,year2gusungrate0,year2junggamrate0,year3money0,year3gusungrate0,year3junggamrate0]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def tbl_sonik_data(self,code,dscd):
		url='http://asp1.krx.co.kr/servlet/krx.asp.XMLJemu?code='+code
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		i=-1;

		for content in soup.findAll('tbl_sonik_data') :
			i=i+1

			hangmok0= content.get('hangmok'+str(i))
			year1money0= content.get('year1money'+str(i))
			year1gusungrate0= content.get('year1gusungrate'+str(i))
			year1junggamrate0= content.get('year1junggamrate'+str(i))
			year2money0= content.get('year2money'+str(i))
			year2gusungrate0= content.get('year2gusungrate'+str(i))
			year2junggamrate0= content.get('year2junggamrate'+str(i))
			year3money0= content.get('year3money'+str(i))
			year3gusungrate0= content.get('year3gusungrate'+str(i))
			year3junggamrate0= content.get('year3junggamrate'+str(i))
			key =['hangmok0','year1money0','year1gusungrate0','year1junggamrate0','year2money0','year2gusungrate0','year2junggamrate0','year3money0','year3gusungrate0','year3junggamrate0']
			value=[hangmok0,year1money0,year1gusungrate0,year1junggamrate0,year2money0,year2gusungrate0,year2junggamrate0,year3money0,year3gusungrate0,year3junggamrate0]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response

	def tbl_cashflow_data(self,code,dscd):
		url='http://asp1.krx.co.kr/servlet/krx.asp.XMLJemu?code='+code
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		i=-1;
		for content in soup.findAll('tbl_cashflow_data') :
			i=i+1
			hangmok0= content.get('hangmok'+str(i))
			year1money0= content.get('year1money'+str(i))
			year1gusungrate0= content.get('year1gusungrate'+str(i))
			year1junggamrate0= content.get('year1junggamrate'+str(i))
			year2money0= content.get('year2money'+str(i))
			year2gusungrate0= content.get('year2gusungrate'+str(i))
			year2junggamrate0= content.get('year2junggamrate'+str(i))
			year3money0= content.get('year3money'+str(i))
			year3gusungrate0= content.get('year3gusungrate'+str(i))
			year3junggamrate0= content.get('year3junggamrate'+str(i))
			key =['hangmok0','year1money0','year1gusungrate0','year1junggamrate0','year2money0','year2gusungrate0','year2junggamrate0','year3money0','year3gusungrate0','year3junggamrate0']
			value=[hangmok0,year1money0,year1gusungrate0,year1junggamrate0,year2money0,year2gusungrate0,year2junggamrate0,year3money0,year3gusungrate0,year3junggamrate0]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response
	def krx_jemu(self,code,dscd):
		url='http://asp1.krx.co.kr/servlet/krx.asp.XMLJemu?code='+code
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		i=-1;

		for content in soup.findAll('tbl_daecha_data') :
			i=i+1

			hangmok0= content.get('hangmok'+str(i))
			year1money0= content.get('year1money'+str(i))
			year1gusungrate0= content.get('year1gusungrate'+str(i))
			year1junggamrate0= content.get('year1junggamrate'+str(i))
			year2money0= content.get('year2money'+str(i))
			year2gusungrate0= content.get('year2gusungrate'+str(i))
			year2junggamrate0= content.get('year2junggamrate'+str(i))
			year3money0= content.get('year3money'+str(i))
			year3gusungrate0= content.get('year3gusungrate'+str(i))
			year3junggamrate0= content.get('year3junggamrate'+str(i))
			key =['hangmok0','year1money0','year1gusungrate0','year1junggamrate0','year2money0','year2gusungrate0','year2junggamrate0','year3money0','year3gusungrate0','year3junggamrate0']
			value=[hangmok0,year1money0,year1gusungrate0,year1junggamrate0,year2money0,year2gusungrate0,year2junggamrate0,year3money0,year3gusungrate0,year3junggamrate0]
		 	if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		i=-1;
		for content in soup.findAll('tbl_sonik_data') :
			i=i+1

			hangmok0= content.get('hangmok'+str(i))
			year1money0= content.get('year1money'+str(i))
			year1gusungrate0= content.get('year1gusungrate'+str(i))
			year1junggamrate0= content.get('year1junggamrate'+str(i))
			year2money0= content.get('year2money'+str(i))
			year2gusungrate0= content.get('year2gusungrate'+str(i))
			year2junggamrate0= content.get('year2junggamrate'+str(i))
			year3money0= content.get('year3money'+str(i))
			year3gusungrate0= content.get('year3gusungrate'+str(i))
			year3junggamrate0= content.get('year3junggamrate'+str(i))
			key =['hangmok0','year1money0','year1gusungrate0','year1junggamrate0','year2money0','year2gusungrate0','year2junggamrate0','year3money0','year3gusungrate0','year3junggamrate0']
			value=[hangmok0,year1money0,year1gusungrate0,year1junggamrate0,year2money0,year2gusungrate0,year2junggamrate0,year3money0,year3gusungrate0,year3junggamrate0]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		i=-1;
		for content in soup.findAll('tbl_cashflow_data') :
			i=i+1

			hangmok0= content.get('hangmok'+str(i))
			year1money0= content.get('year1money'+str(i))
			year1gusungrate0= content.get('year1gusungrate'+str(i))
			year1junggamrate0= content.get('year1junggamrate'+str(i))
			year2money0= content.get('year2money'+str(i))
			year2gusungrate0= content.get('year2gusungrate'+str(i))
			year2junggamrate0= content.get('year2junggamrate'+str(i))
			year3money0= content.get('year3money'+str(i))
			year3gusungrate0= content.get('year3gusungrate'+str(i))
			year3junggamrate0= content.get('year3junggamrate'+str(i))
			key =['hangmok0','year1money0','year1gusungrate0','year1junggamrate0','year2money0','year2gusungrate0','year2junggamrate0','year3money0','year3gusungrate0','year3junggamrate0']
			value=[hangmok0,year1money0,year1gusungrate0,year1junggamrate0,year2money0,year2gusungrate0,year2junggamrate0,year3money0,year3gusungrate0,year3junggamrate0]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def krx_gongsi(self,code,dscd):
		url='http://asp1.krx.co.kr/servlet/krx.asp.DisList4MainServlet?code='+code+'&gubun=K'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		for content in soup.findAll('disinfo') :
			distime= content.get('distime')
			disacpt_no= content.get('disacpt_no')
			distitle= content.get('distitle')
			submitoblgnm= content.get('submitoblgnm')
			key =['distime','disacpt_no','distitle','submitoblgnm']
			value=[distime,disacpt_no,distitle,submitoblgnm]
			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			else:
				response.append(value)
		return response


	def management(self,dscd):
		url='http://finance.naver.com/sise/management.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		# print soup
		for content in soup.findAll('tr')[2:] :

			if len(content.findAll('td')) != 1:
				no=content.findAll('td')[0].text.encode('utf-8')
				title=content.findAll('td')[1].text.encode('utf-8')
				number1=content.findAll('td')[2].text.encode('utf-8')
				number2=content.findAll('td')[3].text.encode('utf-8')
				number3=content.findAll('td')[4].text.encode('utf-8')
				number4=content.findAll('td')[5].text.encode('utf-8')
				center=content.findAll('td')[6].text.encode('utf-8')
				text=content.findAll('td')[7].text.encode('utf-8')
				key =['no','title','number1','number2','number3','number4','center','text']
				value=[no,title,number1,number2,number3,number4,center,text]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,center,text]
					sql="insert into stok0000 (base_dt,no,title,number1,number2,number3,number4,center,text) values (:1,:2,:3,:4,:5,:6,:7,:8,:9)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response


	def trading_halt(self,dscd):
		url='http://finance.naver.com/sise/trading_halt.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		# print soup
		for content in soup.findAll('tr')[2:] :

			if len(content.findAll('td')) != 1:
				no=content.findAll('td')[0].text.encode('utf-8')
				title=content.findAll('td')[1].text.encode('utf-8')
				center=content.findAll('td')[2].text.encode('utf-8')
				text=content.findAll('td')[3].text.encode('utf-8')

				key =['no','title','center','text']
				value=[no,title,center,text]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),no,title,center,text]
					sql="insert into stok0001 (base_dt,no,title,center,text) values (:1,:2,:3,:4,:5)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response

	def investment_alert(self,dscd):
		url='http://finance.naver.com/sise/investment_alert.nhn?type=caution'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		# print soup
		for content in soup.findAll('tr')[2:] :

			if len(content.findAll('td')) != 1:
				no=content.findAll('td')[0].text.encode('utf-8')
				title=content.findAll('td')[1].text.encode('utf-8')
				number1=content.findAll('td')[2].text.encode('utf-8')
				number2=content.findAll('td')[3].text.encode('utf-8')
				number3=content.findAll('td')[4].text.encode('utf-8')
				number4=content.findAll('td')[5].text.encode('utf-8')
				number5=content.findAll('td')[6].text.encode('utf-8')
				number6=content.findAll('td')[7].text.encode('utf-8')
				number7=content.findAll('td')[8].text.encode('utf-8')
				key =['no','title','number1','number2','number3','number4','number5','number6','number7']
				value=[no,title,number1,number2,number3,number4,number5,number6,number7]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7]
					sql="insert into stok0002 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response



	def item_gold(self,dscd):
		url='http://finance.naver.com/sise/item_gold.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		# print soup
		for content in soup.findAll('tr')[7:] :

			if len(content.findAll('td')) != 1:
				no=content.findAll('td')[0].text.encode('utf-8')
				title=content.findAll('td')[1].text.encode('utf-8')
				number1=content.findAll('td')[2].text.encode('utf-8')
				number2=content.findAll('td')[3].text.encode('utf-8')
				number3=content.findAll('td')[4].text.encode('utf-8')
				number4=content.findAll('td')[5].text.encode('utf-8')
				number5=content.findAll('td')[6].text.encode('utf-8')
				number6=content.findAll('td')[7].text.encode('utf-8')
				number7=content.findAll('td')[8].text.encode('utf-8')
				number8=content.findAll('td')[9].text.encode('utf-8')
				number9=content.findAll('td')[10].text.encode('utf-8')
				key =['no','title','number1','number2','number3','number4','number5','number6','number7','number8','number9']
				value=[no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9]
					sql="insert into stok0003 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response


	def item_gap(self,dscd):
		url='http://finance.naver.com/sise/item_gap.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		# print soup
		for content in soup.findAll('tr')[7:] :

			if len(content.findAll('td')) != 1:
				no=content.findAll('td')[0].text.encode('utf-8')
				title=content.findAll('td')[1].text.encode('utf-8')
				number1=content.findAll('td')[2].text.encode('utf-8')
				number2=content.findAll('td')[3].text.encode('utf-8')
				number3=content.findAll('td')[4].text.encode('utf-8')
				number4=content.findAll('td')[5].text.encode('utf-8')
				number5=content.findAll('td')[6].text.encode('utf-8')
				number6=content.findAll('td')[7].text.encode('utf-8')
				number7=content.findAll('td')[8].text.encode('utf-8')
				number8=content.findAll('td')[9].text.encode('utf-8')
				number9=content.findAll('td')[10].text.encode('utf-8')
				key =['no','title','number1','number2','number3','number4','number5','number6','number7','number8','number9']
				value=[no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9]
					sql="insert into stok0004 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response


	def item_igyuk(self,dscd):
		url='http://finance.naver.com/sise/item_igyuk.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		# print soup
		for content in soup.findAll('tr')[7:] :

			if len(content.findAll('td')) != 1:
				no=content.findAll('td')[0].text.encode('utf-8')
				title=content.findAll('td')[1].text.encode('utf-8')
				number1=content.findAll('td')[2].text.encode('utf-8')
				number2=content.findAll('td')[3].text.encode('utf-8')
				number3=content.findAll('td')[4].text.encode('utf-8')
				number4=content.findAll('td')[5].text.encode('utf-8')
				number5=content.findAll('td')[6].text.encode('utf-8')
				number6=content.findAll('td')[7].text.encode('utf-8')
				number7=content.findAll('td')[8].text.encode('utf-8')
				number8=content.findAll('td')[9].text.encode('utf-8')
				number9=content.findAll('td')[10].text.encode('utf-8')
				key =['no','title','number1','number2','number3','number4','number5','number6','number7','number8','number9']
				value=[no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9]
					sql="insert into stok0005 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response

	def item_overheating_1(self,dscd):
		url='http://finance.naver.com/sise/item_overheating_1.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		# print soup
		for content in soup.findAll('tr')[7:] :

			if len(content.findAll('td')) != 1:
				no=content.findAll('td')[0].text.encode('utf-8')
				title=content.findAll('td')[1].text.encode('utf-8')
				number1=content.findAll('td')[2].text.encode('utf-8')
				number2=content.findAll('td')[3].text.encode('utf-8')
				number3=content.findAll('td')[4].text.encode('utf-8')
				number4=content.findAll('td')[5].text.encode('utf-8')
				number5=content.findAll('td')[6].text.encode('utf-8')
				number6=content.findAll('td')[7].text.encode('utf-8')
				number7=content.findAll('td')[8].text.encode('utf-8')
				number8=content.findAll('td')[9].text.encode('utf-8')
				number9=content.findAll('td')[10].text.encode('utf-8')
				key =['no','title','number1','number2','number3','number4','number5','number6','number7','number8','number9']
				value=[no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9]
					sql="insert into stok0006 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response


	def item_overheating_2(self,dscd):
		url='http://finance.naver.com/sise/item_overheating_2.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		# print soup
		for content in soup.findAll('tr')[7:] :

			if len(content.findAll('td')) != 1:
				no=content.findAll('td')[0].text.encode('utf-8')
				title=content.findAll('td')[1].text.encode('utf-8')
				number1=content.findAll('td')[2].text.encode('utf-8')
				number2=content.findAll('td')[3].text.encode('utf-8')
				number3=content.findAll('td')[4].text.encode('utf-8')
				number4=content.findAll('td')[5].text.encode('utf-8')
				number5=content.findAll('td')[6].text.encode('utf-8')
				number6=content.findAll('td')[7].text.encode('utf-8')
				number7=content.findAll('td')[8].text.encode('utf-8')
				number8=content.findAll('td')[9].text.encode('utf-8')
				number9=content.findAll('td')[10].text.encode('utf-8')
				key =['no','title','number1','number2','number3','number4','number5','number6','number7','number8','number9']
				value=[no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9]
					sql="insert into stok0007 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response

	def sise_foreign_hold(self,dscd):
		url='http://finance.naver.com/sise/sise_foreign_hold.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		# print soup
		for content in soup.findAll('tr')[7:] :

			if len(content.findAll('td')) != 1:
				no=content.findAll('td')[0].text.encode('utf-8')
				title=content.findAll('td')[1].text.encode('utf-8')
				number1=content.findAll('td')[2].text.encode('utf-8')
				number2=content.findAll('td')[3].text.encode('utf-8')
				number3=content.findAll('td')[4].text.encode('utf-8')
				number4=content.findAll('td')[5].text.encode('utf-8')
				number5=content.findAll('td')[6].text.encode('utf-8')
				number6=content.findAll('td')[7].text.encode('utf-8')
				number7=content.findAll('td')[8].text.encode('utf-8')
				number8=content.findAll('td')[9].text.encode('utf-8')

				key =['no','title','number1','number2','number3','number4','number5','number6','number7','number8']
				value=[no,title,number1,number2,number3,number4,number5,number6,number7,number8]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8]
					sql="insert into stok0008 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response


	def sise_quant_0(self,dscd):
		url='http://finance.naver.com/sise/sise_quant.nhn?sosok=0'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll('tr')[7:] :

			if len(content.findAll('td')) != 1:
				no=content.findAll('td')[0].text.encode('utf-8')
				title=content.findAll('td')[1].text.encode('utf-8')
				number1=content.findAll('td')[2].text.encode('utf-8')
				number2=content.findAll('td')[3].text.encode('utf-8')
				number3=content.findAll('td')[4].text.encode('utf-8')
				number4=content.findAll('td')[5].text.encode('utf-8')
				number5=content.findAll('td')[6].text.encode('utf-8')
				number6=content.findAll('td')[7].text.encode('utf-8')
				number7=content.findAll('td')[8].text.encode('utf-8')
				number8=content.findAll('td')[9].text.encode('utf-8')
				number9=content.findAll('td')[10].text.encode('utf-8')
				number10=content.findAll('td')[11].text.encode('utf-8')
				key =['no','title','number1','number2','number3','number4','number5','number6','number7','number8','number9','number10']
				value=[no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),'00',no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10]
					sql="insert into stok0009 (base_dt,market,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response

	def sise_quant_1(self,dscd):
		url='http://finance.naver.com/sise/sise_quant.nhn?sosok=1'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll('tr')[7:] :

			if len(content.findAll('td')) != 1:
				no=content.findAll('td')[0].text.encode('utf-8')
				title=content.findAll('td')[1].text.encode('utf-8')
				number1=content.findAll('td')[2].text.encode('utf-8')
				number2=content.findAll('td')[3].text.encode('utf-8')
				number3=content.findAll('td')[4].text.encode('utf-8')
				number4=content.findAll('td')[5].text.encode('utf-8')
				number5=content.findAll('td')[6].text.encode('utf-8')
				number6=content.findAll('td')[7].text.encode('utf-8')
				number7=content.findAll('td')[8].text.encode('utf-8')
				number8=content.findAll('td')[9].text.encode('utf-8')
				number9=content.findAll('td')[10].text.encode('utf-8')
				number10=content.findAll('td')[11].text.encode('utf-8')
				key =['no','title','number1','number2','number3','number4','number5','number6','number7','number8','number9','number10']
				value=[no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),'01',no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10]
					sql="insert into stok0009 (base_dt,market,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response

	def sise_upper(self,dscd):
		url='http://finance.naver.com/sise/sise_upper.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll('tr')[7:] :

			if len(content.findAll('td')) != 1 and len(content.findAll('th')) ==0:

				no=content.findAll('td')[0].text.encode('utf-8')
				number1=content.findAll('td')[1].text.encode('utf-8')
				number2=content.findAll('td')[2].text.encode('utf-8')
				title=content.findAll('td')[3].text.encode('utf-8')
				number3=content.findAll('td')[4].text.encode('utf-8')
				number4=content.findAll('td')[5].text.encode('utf-8')
				number5=content.findAll('td')[6].text.encode('utf-8')
				number6=content.findAll('td')[7].text.encode('utf-8')
				number7=content.findAll('td')[8].text.encode('utf-8')
				number8=content.findAll('td')[9].text.encode('utf-8')
				number9=content.findAll('td')[10].text.encode('utf-8')
				number10=content.findAll('td')[11].text.encode('utf-8')
				key =['no','title','number1','number2','number3','number4','number5','number6','number7','number8','number9','number10']
				value=[no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10]
					sql="insert into stok0010 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response

	def sise_lower(self,dscd):
		url='http://finance.naver.com/sise/sise_lower.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll('tr')[7:] :

			if len(content.findAll('td')) != 1 and len(content.findAll('th')) ==0:

				no=content.findAll('td')[0].text.encode('utf-8')
				number1=content.findAll('td')[1].text.encode('utf-8')
				number2=content.findAll('td')[2].text.encode('utf-8')
				title=content.findAll('td')[3].text.encode('utf-8')
				number3=content.findAll('td')[4].text.encode('utf-8')
				number4=content.findAll('td')[5].text.encode('utf-8')
				number5=content.findAll('td')[6].text.encode('utf-8')
				number6=content.findAll('td')[7].text.encode('utf-8')
				number7=content.findAll('td')[8].text.encode('utf-8')
				number8=content.findAll('td')[9].text.encode('utf-8')
				number9=content.findAll('td')[10].text.encode('utf-8')
				number10=content.findAll('td')[11].text.encode('utf-8')
				key =['no','title','number1','number2','number3','number4','number5','number6','number7','number8','number9','number10']
				value=[no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10]
					sql="insert into stok0011 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response


	def sise_upjong_t(self,dscd):
		url='http://sise.wownet.co.kr/nude/sise/stockPlus.asp?bcode=N02011000&mseq=1531&gubun=T'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll('tr')[1:] :

			if len(content.findAll('td')) != 1 and len(content.findAll('th')) ==0:

				title=content.findAll('td')[0].text.encode('utf-8')
				number1=content.findAll('td')[1].text.encode('utf-8')
				number2=content.findAll('td')[2].text.encode('utf-8')
				number3=content.findAll('td')[3].text.encode('utf-8')
				number4=content.findAll('td')[4].text.encode('utf-8')
				number5=content.findAll('td')[5].text.encode('utf-8')
				number6=content.findAll('td')[6].text.encode('utf-8')
				number7=content.findAll('td')[7].text.encode('utf-8')
				number8=content.findAll('td')[8].text.encode('utf-8')
				key =['title','number1','number2','number3','number4','number5','number6','number7','number8']
				value=[title,number1,number2,number3,number4,number5,number6,number7,number8]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),title,number1,number2,number3,number4,number5,number6,number7,number8]
					sql="insert into stok0012 (base_dt,title,number1,number2,number3,number4,number5,number6,number7,number8) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response

	def sise_upjong_t(self,dscd):
		url='http://sise.wownet.co.kr/nude/sise/stockPlus.asp?bcode=N02011000&mseq=1531&gubun=K'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll('tr')[1:] :

			if len(content.findAll('td')) != 1 and len(content.findAll('th')) ==0:

				title=content.findAll('td')[0].text.encode('utf-8')
				number1=content.findAll('td')[1].text.encode('utf-8')
				number2=content.findAll('td')[2].text.encode('utf-8')
				number3=content.findAll('td')[3].text.encode('utf-8')
				number4=content.findAll('td')[4].text.encode('utf-8')
				number5=content.findAll('td')[5].text.encode('utf-8')
				number6=content.findAll('td')[6].text.encode('utf-8')
				number7=content.findAll('td')[7].text.encode('utf-8')
				number8=content.findAll('td')[8].text.encode('utf-8')
				key =['title','number1','number2','number3','number4','number5','number6','number7','number8']
				value=[title,number1,number2,number3,number4,number5,number6,number7,number8]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),title,number1,number2,number3,number4,number5,number6,number7,number8]
					sql="insert into stok0013 (base_dt,title,number1,number2,number3,number4,number5,number6,number7,number8) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response

	def ipo_chyounggu(self,dscd):
		url='http://www.ipo38.co.kr/ipo/index.htm?key=1'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll('tr')[25:] :

			if len(content.findAll('td')) == 8 :

				basedt=content.findAll('td')[0].text.encode('utf-8')
				title=content.findAll('td')[1].text.encode('utf-8')
				status=content.findAll('td')[2].text.encode('utf-8')
				price=content.findAll('td')[3].text.encode('utf-8')
				number1=content.findAll('td')[4].text.encode('utf-8')
				number2=content.findAll('td')[5].text.encode('utf-8')
				number3=content.findAll('td')[6].text.encode('utf-8').replace('&nbsp;','')
				upjgong=content.findAll('td')[7].text.encode('utf-8')

				key =['basedt','title','status','price','number1','number2','number3','upjgong']
				value=[basedt,title,status,price,number1,number2,number3,upjgong]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),basedt,title,status,price,number1,number2,number3,upjgong]
					sql="insert into stok0014 (base_dt,basedt,title,status,price,number1,number2,number3,upjgong) values (:1,:2,:3,:4,:5,:6,:7,:8,:9)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response

	def ipo_permission(self,dscd):
		url='http://www.ipo38.co.kr/ipo/index.htm?key=2'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll('tr')[25:] :

			if len(content.findAll('td')) == 8 :

				basedt=content.findAll('td')[0].text.encode('utf-8')
				title=content.findAll('td')[1].text.encode('utf-8')
				status=content.findAll('td')[2].text.encode('utf-8')
				price=content.findAll('td')[3].text.encode('utf-8')
				number1=content.findAll('td')[4].text.encode('utf-8')
				number2=content.findAll('td')[5].text.encode('utf-8')
				number3=content.findAll('td')[6].text.encode('utf-8').replace('&nbsp;','')
				upjgong=content.findAll('td')[7].text.encode('utf-8')

				key =['basedt','title','status','price','number1','number2','number3','upjgong']
				value=[basedt,title,status,price,number1,number2,number3,upjgong]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),basedt,title,status,price,number1,number2,number3,upjgong]
					sql="insert into stok0015 (base_dt,basedt,title,status,price,number1,number2,number3,upjgong) values (:1,:2,:3,:4,:5,:6,:7,:8,:9)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response

	def ipo_ir(self,dscd):
		url='http://www.ipo38.co.kr/ipo/index.htm?key=3'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll('tr')[25:] :

			if len(content.findAll('td')) == 5 :
				title=content.findAll('td')[0].text.encode('utf-8')
				basedt=content.findAll('td')[1].text.encode('utf-8')
				addr=content.findAll('td')[2].text.encode('utf-8').replace('&nbsp;','')
				price=content.findAll('td')[3].text.encode('utf-8')
				enterprise=content.findAll('td')[4].text.encode('utf-8')
				key =['title','basedt','addr',',price','enterprise']
				value=[title,basedt,addr,price,enterprise]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),title,basedt,addr,price,enterprise]
					sql="insert into stok0016 (base_dt,title,basedt,addr,price,enterprise) values (:1,:2,:3,:4,:5,:6)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response

	def ipo_suyo_predict(self,dscd):
		url='http://www.ipo38.co.kr/ipo/index.htm?key=4'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll('tr')[25:] :

			if len(content.findAll('td')) == 6:
				title=content.findAll('td')[0].text.encode('utf-8').replace('&nbsp;','')
				basedt=content.findAll('td')[1].text.encode('utf-8')
				want_gongmoga=content.findAll('td')[2].text.encode('utf-8').replace('&nbsp;','')
				fix_gongmoga=content.findAll('td')[3].text.encode('utf-8')
				total_gongmoga=content.findAll('td')[4].text.encode('utf-8')
				enterprise=content.findAll('td')[5].text.encode('utf-8')

				key =['title','basedt','want_gongmoga','fix_gongmoga','total_gongmoga','enterprise']
				value=[title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,enterprise]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,enterprise]
					sql="insert into stok0017 (base_dt,title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,enterprise) values (:1,:2,:3,:4,:5,:6,:7)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response
	def ipo_suyo_result(self,dscd):
		url='http://www.ipo38.co.kr/ipo/index.htm?key=5'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll('tr')[25:] :

			if len(content.findAll('td')) == 8:
				title=content.findAll('td')[0].text.encode('utf-8')
				basedt=content.findAll('td')[1].text.encode('utf-8')
				want_gongmoga=content.findAll('td')[2].text.encode('utf-8').replace('&nbsp;','')
				fix_gongmoga=content.findAll('td')[3].text.encode('utf-8')
				total_gongmoga=content.findAll('td')[4].text.encode('utf-8')
				competetion=content.findAll('td')[5].text.encode('utf-8')
				percent=content.findAll('td')[6].text.encode('utf-8')
				enterprise=content.findAll('td')[7].text.encode('utf-8')

				key =['title','basedt','want_gongmoga','fix_gongmoga','total_gongmoga','competetion','percent','enterprise']
				value=[title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,competetion,percent,enterprise]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,competetion,percent,enterprise]
					sql="insert into stok0018 (base_dt,title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,competetion,percent,enterprise) values (:1,:2,:3,:4,:5,:6,:7,:8,:9)"

					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response
	def ipo_gongmo(self,dscd):
		url='http://www.ipo38.co.kr/ipo/index.htm?key=6'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll('tr')[25:] :

			if len(content.findAll('td')) == 7 and len(content.findAll('table')) == 0:

				title=content.findAll('td')[0].text.encode('utf-8').replace('&nbsp;','')
				basedt=content.findAll('td')[1].text.encode('utf-8')
				want_gongmoga=content.findAll('td')[2].text.encode('utf-8')
				fix_gongmoga=content.findAll('td')[3].text.encode('utf-8')
				total_gongmoga=content.findAll('td')[4].text.encode('utf-8')
				competetion=content.findAll('td')[5].text.encode('utf-8')

				enterprise=content.findAll('td')[6].text.encode('utf-8')

				key =['title','basedt','want_gongmoga','fix_gongmoga','total_gongmoga','competetion','enterprise']
				value=[title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,competetion,enterprise]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,competetion,enterprise]
					sql="insert into stok0019 (base_dt,title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,competetion,enterprise) values (:1,:2,:3,:4,:5,:6,:7,:8)"
					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response
	def ipo_new(self,dscd):
		url='http://www.ipo38.co.kr/ipo/index.htm?key=7'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll('tr')[25:] :

			if len(content.findAll('td')) == 10:

				title=content.findAll('td')[0].text.encode('utf-8')
				basedt=content.findAll('td')[1].text.encode('utf-8')
				number1=content.findAll('td')[2].text.encode('utf-8').replace('&nbsp;','')
				number2=content.findAll('td')[3].text.encode('utf-8').replace('&nbsp;','')
				number3=content.findAll('td')[4].text.encode('utf-8').replace('&nbsp;','')
				number4=content.findAll('td')[5].text.encode('utf-8').replace('&nbsp;','')
				number5=content.findAll('td')[6].text.encode('utf-8').replace('&nbsp;','')
				number6=content.findAll('td')[7].text.encode('utf-8').replace('&nbsp;','')
				number7=content.findAll('td')[8].text.encode('utf-8').replace('&nbsp;','')
				number8=content.findAll('td')[9].text.encode('utf-8').replace('&nbsp;','')
				key =['title','basedt','number1','number2','number3','number4','number5','number6','number7','number8']
				value=[title,basedt,number1,number2,number3,number4,number5,number6,number7,number8]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),title,basedt,number1,number2,number3,number4,number5,number6,number7,number8]
					sql="insert into stok0020 (base_dt,title,basedt,number1,number2,number3,number4,number5,number6,number7,number8) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)"
					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response

	def ipo_cbbw(self,dscd):
		url='http://www.ipo38.co.kr/fund/'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll('tr')[25:-18] :
			if len(content.findAll('td')) == 9:
				mk_dscd=content.findAll('td')[0].text.encode('utf-8')
				basedt=content.findAll('td')[1].text.encode('utf-8')
				title=content.findAll('td')[2].text.encode('utf-8')
				number2=content.findAll('td')[3].text.encode('utf-8')
				number3=content.findAll('td')[4].text.encode('utf-8')
				number4=content.findAll('td')[5].text.encode('utf-8')
				number5=content.findAll('td')[6].text.encode('utf-8')
				enterprise=content.findAll('td')[7].text.encode('utf-8')
				event_dt=content.findAll('td')[8].text.encode('utf-8')

				key =['mk_dscd','basedt','title','number2','number3','number4','number5','enterprise','event_dt']
				value=[mk_dscd,basedt,title,number2,number3,number4,number5,enterprise,event_dt]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":
					value=[dao.yyyymmdd(),mk_dscd,basedt,title,number2,number3,number4,number5,enterprise,event_dt]
					sql="insert into stok0021 (base_dt,dscd,basedt,title,number2,number3,number4,number5,enterprise,event_dt) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)"
					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response


	def ipo_ilban(self,dscd):
		url='http://www.ipo38.co.kr/fund1/'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		for content in soup.findAll('tr')[25:-18] :

			if len(content.findAll('td')) == 9 :
				title=content.findAll('td')[0].text.encode('utf-8').replace('&nbsp;','')
				mk_dscd=content.findAll('td')[1].text.encode('utf-8').replace('&nbsp;','')
				basedt=content.findAll('td')[2].text.encode('utf-8')
				number2=content.findAll('td')[3].text.encode('utf-8')
				number3=content.findAll('td')[4].text.encode('utf-8')
				number4=content.findAll('td')[5].text.encode('utf-8')
				number5=content.findAll('td')[6].text.encode('utf-8')
				number6=content.findAll('td')[7].text.encode('utf-8')
				enterprise=content.findAll('td')[8].text.encode('utf-8')

				key =['title','mk_dscd','basedt','number2','number3','number4','number5','number6','enterprise']
				value=[title,mk_dscd,basedt,number2,number3,number4,number5,number6,enterprise]

				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				elif dscd == "B":

					value=[dao.yyyymmdd(),title,mk_dscd,basedt,number2,number3,number4,number5,number6,enterprise]
					sql="insert into stok0022 (base_dt,title,dscd,basedt,number2,number3,number4,number5,number6,enterprise) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)"
					rp=dao.insert(sql,value)
					response.append(rp)
				else:
					response.append(value)
		return response



	def munji(self,dscd):
		url='http://cleanair.seoul.go.kr/air_city.htm?method=measure&grp1=pm10'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]

		# print soup
		for content in soup.findAll('tr')[11:] :

			title=content.findAll('td')[0].text.encode('utf-8').replace('&nbsp;','')
			mise=content.findAll('td')[1].text.encode('utf-8')
			chomise=content.findAll('td')[2].text.encode('utf-8')
			ozone=content.findAll('td')[3].text.encode('utf-8')
			esan=content.findAll('td')[4].text.encode('utf-8')
			ilsan=content.findAll('td')[5].text.encode('utf-8')
			awhang=content.findAll('td')[6].text.encode('utf-8')
			grade=content.findAll('td')[7].text.encode('utf-8')
			jisu=content.findAll('td')[8].text.encode('utf-8')
			material=content.findAll('td')[9].text.encode('utf-8')
			key =['title','mise','chomise','ozone','esan','ilsan','awhang','grade','jisu','material']
			value=[title,mise,chomise,ozone,esan,ilsan,awhang,grade,jisu,material]

			if dscd == "json":
				result=dict(zip(key,value))
				response.append(result)
			elif dscd == "B":
				value=[dao.yyyymmdd(),title,mise,chomise,ozone,esan,ilsan,awhang,grade,jisu,material]
				sql="insert into news0003 (base_dt,title,mise,chomise,ozone,esan,ilsan,awhang,grade,jisu,material) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)"
				rp=dao.insert(sql,value)
				response.append(rp)
			else:
				response.append(value)
		return response


	def sise_group(self,dscd):
		url='http://finance.naver.com/sise/sise_group.nhn?type=group'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]


		for content in soup.findAll('tr')[1:] :
			if len(content.findAll('td')) == 7 and len(content.findAll('th')) ==0:
				title=content.findAll('td')[0].text.encode('utf-8')
				number1=content.findAll('td')[1].text.encode('utf-8')
				number2=content.findAll('td')[2].text.encode('utf-8')
				number3=content.findAll('td')[3].text.encode('utf-8')
				number4=content.findAll('td')[4].text.encode('utf-8')
				number5=content.findAll('td')[5].text.encode('utf-8')

				key =['title','number1','number2','number3','number4','number5']
				value=[title,number1,number2,number3,number4,number5]
				if dscd == "json":
					result=dict(zip(key,value))
					response.append(result)
				else:
					response.append(value)
		return response