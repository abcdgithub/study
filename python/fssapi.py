# -*- coding: utf-8 -*-
import config
import util
from bs4 import BeautifulSoup

class fssapi:
	authKey=config.apikey002
	#금융쿨팁 200선 api
	def tip(self,apiType,startDate,endDate):
		url="http://www.fss.or.kr/fss/kr/openApi/api/tip.jsp?apiType=%s&startDate=%s&endDate=%s&authKey=%s" %(apiType,startDate,endDate ,self.authKey)
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		if apiType =="json" :
			return r;
		for content in soup.findAll('result') :
			contentid= content.find('contentid').text
			policyType= content.find('policyType').text
			brmTrans= content.find('brmTrans').text
			brmCode= content.find('brmCode').text
			repcategory= content.find('repcategory').text
			subject= content.find('subject').text
			publishOrg= content.find('publishOrg').text
			originUrl= content.find('originUrl').text
			viewCnt= content.find('viewCnt').text
			regDate= content.find('regDate').text
			atchfileUrl= content.find('atchfileUrl').text
			atchfileNm= content.find('atchfileNm').text
			contentsKor= content.find('contentsKor').text
			temp1= content.find('temp1').text
			lists= content.find('lists').text
			key=   ['contentid','policyType','brmTrans','brmCode','repcategory','subject','publishOrg','originUrl','viewCnt','regDate','atchfileUrl','atchfileNm','contentsKor','temp1','lists']
			value= [contentid,policyType,brmTrans,brmCode,repcategory,subject,publishOrg,originUrl,viewCnt,regDate,atchfileUrl,atchfileNm,contentsKor,temp1,lists]
			response.append(value)
		return response
	#금융소비자뉴스
	def fcnInfo(self,apiType,startDate,endDate):
		url="http://www.fss.or.kr/fss/kr/openApi/api/fcnInfo.jsp?apiType=%s&startDate=%s&endDate=%s&authKey=%s" %(apiType,startDate,endDate ,self.authKey)
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		if apiType =="json" :
			return r;
		for content in soup.findAll('result') :
			contentid= content.find('contentid').text
			subject= content.find('subject').text
			publishOrg= content.find('publishOrg').text
			originUrl= content.find('originUrl').text
			viewCnt= content.find('viewCnt').text
			regDate= content.find('regDate').text
			atchfileUrl= content.find('atchfileUrl').text
			atchfileNm= content.find('atchfileNm').text
			contentsKor= content.find('contentsKor').text
			key=   ['contentid','subject','publishOrg','originUrl','viewCnt','regDate','atchfileUrl','atchfileNm','contentsKor']
			value= [contentid,subject,publishOrg,originUrl,viewCnt,regDate,atchfileUrl,atchfileNm,contentsKor]
			response.append(value)
		return response
	#보도자료
	def bodoInfo(self,apiType,startDate,endDate):
		url="http://www.fss.or.kr/fss/kr/openApi/api/bodoInfo.jsp?apiType=%s&startDate=%s&endDate=%s&authKey=%s" %(apiType,startDate,endDate ,self.authKey)
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		if apiType =="json" :
			return r;
		for content in soup.findAll('result') :
			contentid= content.find('contentid').text
			subject= content.find('subject').text
			publishOrg= content.find('publishOrg').text
			originUrl= content.find('originUrl').text
			viewCnt= content.find('viewCnt').text
			regDate= content.find('regDate').text
			atchfileUrl= content.find('atchfileUrl').text
			atchfileNm= content.find('atchfileNm').text
			contentsKor= content.find('contentsKor').text
			lists= content.find('lists').text
			key=   ['contentid','subject','publishOrg','originUrl','viewCnt','regDate','atchfileUrl','atchfileNm','contentsKor','lists']
			value= [contentid,subject,publishOrg,originUrl,viewCnt,regDate,atchfileUrl,atchfileNm,contentsKor,lists]
			response.append(value)
		return response
	#금융권 채용정보
	def recruitInfo(self,apiType,startDate,endDate):
		url="http://www.fss.or.kr/fss/kr/openApi/api/recruitInfo.jsp?apiType=%s&startDate=%s&endDate=%s&authKey=%s" %(apiType,startDate,endDate ,self.authKey)
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		if apiType =="json" :
			return r;
		for content in soup.findAll('result') :
			appformNo= content.find('appformNo').text
			titl= content.find('titl').text
			instNm= content.find('instNm').text
			induType= content.find('induType').text
			hireFld= content.find('hireFld').text
			hireType= content.find('hireType').text
			hireDiv= content.find('hireDiv').text
			recpStrtDay= content.find('recpStrtDay').text
			recpEndDay= content.find('recpEndDay').text
			updtDate= content.find('updtDate').text
			siteUrl= content.find('siteUrl').text
			hireCntn= content.find('hireCntn').text
			originUrl= content.find('originUrl').text
			key=   ['appformNo','titl','instNm','induType','hireFld','hireType','hireDiv','recpStrtDay','recpEndDay','updtDate','siteUrl','hireCntn','originUrl']
			value= [appformNo,titl,instNm,induType,hireFld,hireType,hireDiv,recpStrtDay,recpEndDay,updtDate,siteUrl,hireCntn,originUrl]
			response.append(value)
		return response	
	#금융시장동향
	def fnncMrkt(self,apiType,startDate,endDate):
		url="http://www.fss.or.kr/fss/kr/openApi/api/fnncMrkt.jsp?apiType=%s&startDate=%s&endDate=%s&authKey=%s" %(apiType,startDate,endDate ,self.authKey)
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		if apiType =="json" :
			return r;
		for content in soup.findAll('result') :
			contentId= content.find('contentId').text
			policyType= content.find('policyType').text
			brmTrans= content.find('brmTrans').text
			brmCode= content.find('brmCode').text
			repcategory= content.find('repcategory').text
			subject= content.find('subject').text
			publishOrg= content.find('publishOrg').text
			originUrl= content.find('originUrl').text
			viewCnt= content.find('viewCnt').text
			regDate= content.find('regDate').text
			atchfileUrl= content.find('atchfileUrl').text
			atchfileNm= content.find('atchfileNm').text
			originUrl= content.find('originUrl').text
			contentsKor= content.find('contentsKor').text
			lists= content.find('lists').text
			key=   ['contentId','policyType','brmTrans','brmCode','repcategory','subject','publishOrg','originUrl','viewCnt','regDate','atchfileUrl','atchfileNm','contentsKor','lists']
			value= [contentId,policyType,brmTrans,brmCode,repcategory,subject,publishOrg,originUrl,viewCnt,regDate,atchfileUrl,atchfileNm,contentsKor,lists]
			response.append(value)
		return response	
	#금융감독정보
	def fnncMngInfo(self,apiType,startDate,endDate):
		url="http://www.fss.or.kr/fss/kr/openApi/api/fnncMngInfo.jsp?apiType=%s&startDate=%s&endDate=%s&authKey=%s" %(apiType,startDate,endDate ,self.authKey)
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		if apiType =="json" :
			return r;
		for content in soup.findAll('result') :
			contentId= content.find('contentId').text
			policyType= content.find('policyType').text
			brmTrans= content.find('brmTrans').text
			brmCode= content.find('brmCode').text
			repcategory= content.find('repcategory').text
			subject= content.find('subject').text
			publishOrg= content.find('publishOrg').text
			originUrl= content.find('originUrl').text
			viewCnt= content.find('viewCnt').text
			regDate= content.find('regDate').text
			atchfileUrl= content.find('atchfileUrl').text
			atchfileNm= content.find('atchfileNm').text
			contentsKor= content.find('contentsKor').text
			lists= content.find('lists').text
			key=   ['contentId','policyType','brmTrans','brmCode','repcategory','subject','publishOrg','originUrl','viewCnt','regDate','atchfileUrl','atchfileNm','contentsKor','lists']
			value= [contentId,policyType,brmTrans,brmCode,repcategory,subject,publishOrg,originUrl,viewCnt,regDate,atchfileUrl,atchfileNm,contentsKor,lists]
			response.append(value)
		return response	
	#금융감독제도 일반
	def fvsttGnrl(self,apiType,startDate,endDate):
		url="http://www.fss.or.kr/fss/kr/openApi/api/fvsttGnrl.jsp?apiType=%s&startDate=%s&endDate=%s&authKey=%s" %(apiType,startDate,endDate ,self.authKey)
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		if apiType =="json" :
			return r;
		for content in soup.findAll('result') :
			contentId= content.find('contentId').text
			policyType= content.find('policyType').text
			brmTrans= content.find('brmTrans').text
			brmCode= content.find('brmCode').text
			repcategory= content.find('repcategory').text
			subject= content.find('subject').text
			publishOrg= content.find('publishOrg').text
			originUrl= content.find('originUrl').text
			viewCnt= content.find('viewCnt').text
			regDate= content.find('regDate').text
			atchfileUrl= content.find('atchfileUrl').text
			atchfileNm= content.find('atchfileNm').text
			contentsKor= content.find('contentsKor').text
			temp1= content.find('temp1').text
			lists= content.find('lists').text
			key=   ['contentId','policyType','brmTrans','brmCode','repcategory','subject','publishOrg','originUrl','viewCnt','regDate','atchfileUrl','atchfileNm','contentsKor','temp1','lists']
			value= [contentId,policyType,brmTrans,brmCode,repcategory,subject,publishOrg,originUrl,viewCnt,regDate,atchfileUrl,atchfileNm,contentsKor,temp1,lists]
			response.append(value)
		return response	
	#분야별 감독제도
	def fealmMng(self,apiType,startDate,endDate):
		url="http://www.fss.or.kr/fss/kr/openApi/api/fealmMng.jsp?apiType=%s&startDate=%s&endDate=%s&authKey=%s" %(apiType,startDate,endDate ,self.authKey)
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		if apiType =="json" :
			return r;
		for content in soup.findAll('result') :
			contentId= content.find('contentId').text
			policyType= content.find('policyType').text
			brmTrans= content.find('brmTrans').text
			brmCode= content.find('brmCode').text
			repcategory= content.find('repcategory').text
			subject= content.find('subject').text
			publishOrg= content.find('publishOrg').text
			originUrl= content.find('originUrl').text
			viewCnt= content.find('viewCnt').text
			regDate= content.find('regDate').text
			atchfileUrl= content.find('atchfileUrl').text
			atchfileNm= content.find('atchfileNm').text
			contentsKor= content.find('contentsKor').text
			temp1= content.find('temp1').text
			lists= content.find('lists').text
			key=   ['contentId','policyType','brmTrans','brmCode','repcategory','subject','publishOrg','originUrl','viewCnt','regDate','atchfileUrl','atchfileNm','contentsKor','temp1','lists']
			value= [contentId,policyType,brmTrans,brmCode,repcategory,subject,publishOrg,originUrl,viewCnt,regDate,atchfileUrl,atchfileNm,contentsKor,temp1,lists]
			response.append(value)
		return response				

	#은행 경영통계
	def bankMngmt(self,apiType,startDate,endDate):
		url="http://www.fss.or.kr/fss/kr/openApi/api/bankMngmt.jsp?apiType=%s&startDate=%s&endDate=%s&authKey=%s" %(apiType,startDate,endDate ,self.authKey)
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		if apiType =="json" :
			return r;
		for content in soup.findAll('result') :
			contentId= content.find('contentId').text
			policyType= content.find('policyType').text
			brmTrans= content.find('brmTrans').text
			brmCode= content.find('brmCode').text
			repcategory= content.find('repcategory').text
			subject= content.find('subject').text
			publishOrg= content.find('publishOrg').text
			originUrl= content.find('originUrl').text
			viewCnt= content.find('viewCnt').text
			regDate= content.find('regDate').text
			atchfileUrl= content.find('atchfileUrl').text
			atchfileNm= content.find('atchfileNm').text
			contentsKor= content.find('contentsKor').text
			lists= content.find('lists').text
			key=   ['contentId','policyType','brmTrans','brmCode','repcategory','subject','publishOrg','originUrl','viewCnt','regDate','atchfileUrl','atchfileNm','contentsKor','lists']
			value= [contentId,policyType,brmTrans,brmCode,repcategory,subject,publishOrg,originUrl,viewCnt,regDate,atchfileUrl,atchfileNm,contentsKor,lists]
			response.append(value)
		return response	

	#외국인 국내 투자동향 API 상세
	def invtTrend(self,apiType,startDate,endDate):
		url="http://www.fss.or.kr/fss/kr/openApi/api/invtTrend.jsp?apiType=%s&startDate=%s&endDate=%s&authKey=%s" %(apiType,startDate,endDate ,self.authKey)
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup(r.content)
		r.close()
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		if apiType =="json" :
			return r;
		for content in soup.findAll('result') :
			contentId= content.find('contentId').text
			policyType= content.find('policyType').text
			brmTrans= content.find('brmTrans').text
			brmCode= content.find('brmCode').text
			repcategory= content.find('repcategory').text
			subject= content.find('subject').text
			publishOrg= content.find('publishOrg').text
			originUrl= content.find('originUrl').text
			viewCnt= content.find('viewCnt').text
			regDate= content.find('regDate').text
			atchfileUrl= content.find('atchfileUrl').text
			atchfileNm= content.find('atchfileNm').text
			contentsKor= content.find('contentsKor').text
			lists= content.find('lists').text
			key=   ['contentId','policyType','brmTrans','brmCode','repcategory','subject','publishOrg','originUrl','viewCnt','regDate','atchfileUrl','atchfileNm','contentsKor','lists']
			value= [contentId,policyType,brmTrans,brmCode,repcategory,subject,publishOrg,originUrl,viewCnt,regDate,atchfileUrl,atchfileNm,contentsKor,lists]
			response.append(value)
		return response			



