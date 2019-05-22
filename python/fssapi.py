# -*- coding: utf-8 -*-
import config
import util

class fssapi:
	authKey=config.apikey002
	#금융쿨팁 200선 api
	def tip(self,apiType,startDate,endDate):
		url="http://www.fss.or.kr/fss/kr/openApi/api/tip.jsp?apiType=%s&startDate=%s&endDate=%s&authKey=%s" %(apiType,startDate,endDate ,self.authKey)
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
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

	def fcnInfo(self,apiType,startDate,endDate):
		url="http://www.fss.or.kr/fss/kr/openApi/api/fcnInfo.jsp?apiType=%s&startDate=%s&endDate=%s&authKey=%s" %(apiType,startDate,endDate ,self.authKey)
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
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

	def bodoInfo(self,apiType,startDate,endDate):
		url="http://www.fss.or.kr/fss/kr/openApi/api/bodoInfo.jsp?apiType=%s&startDate=%s&endDate=%s&authKey=%s" %(apiType,startDate,endDate ,self.authKey)
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
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
	




