# -*- coding: utf8 -*-
import requests, BeautifulSoup,re
from bs4 import BeautifulSoup as bs4
import time
import db
import pymysql
import sys
import win32com.client
import pythoncom


class dbinsert:
	host='127.0.0.1'
	port=3306
	user=''
	passwd=''
	mysql=''
	server_addr = ""
	server_port = ""
	server_type = ""
	user_id = ""
	user_pass = ""
	user_certificate_pass = ""
	def naversearch(self):
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()

		r = requests.get('http://datalab.naver.com/keyword/realtimeList.naver?where=main')
		soup = BeautifulSoup.BeautifulSoup(r.content)
		r.close()
		article=soup.find("div",attrs={'class':"keyword_rank"})
		value =[]
		response =[]
		for content in article.findAll('li' ) :
			sno= content.find('em',attrs={'class':'num'}).text.encode('utf-8')
			title= content.find('span',attrs={'class':'title'}).text.encode('utf-8')
			cursor.execute("insert into news0002 (base_dt,sno,title) values (%s,%s,%s)",(dao.sec(),sno,title))
		mysql.commit()
		cursor.close()
		mysql.close()
		return response

	def management(self):
		url='http://finance.naver.com/sise/management.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)

		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()

		# cursor.execute("set names utf8")
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
				value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,center,text]

				cursor.execute("insert into stok0000 (base_dt,no,title,number1,number2,number3,number4,center,text) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),no,title,number1,number2,number3,number4,center,text))
				# sql="insert into stok0000 (base_dt,no,title,number1,number2,number3,number4,center,text) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
				# mysql.commit()
				#
		mysql.commit()
		cursor.close()
		mysql.close()
		return response


	def trading_halt(self):
		url='http://finance.naver.com/sise/trading_halt.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		# print soup
		for content in soup.findAll('tr')[2:] :
			if len(content.findAll('td')) != 1:
				no=content.findAll('td')[0].text.encode('utf-8')
				title=content.findAll('td')[1].text.encode('utf-8')
				center=content.findAll('td')[2].text.encode('utf-8')
				text=content.findAll('td')[3].text.encode('utf-8')
				value=[dao.yyyymmdd(),no,title,center,text]
				cursor.execute("insert into stok0001 (base_dt,no,title,center,text) values (%s,%s,%s,%s,%s)",(dao.yyyymmdd(),no,title,center,text))
		mysql.commit()
		cursor.close()
		mysql.close()
		return response

	def investment_alert(self):
		url='http://finance.naver.com/sise/investment_alert.nhn?type=caution'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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


				value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7]
				cursor.execute("insert into stok0002 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7))
		mysql.commit()
		cursor.close()
		mysql.close()
		return response



	def item_gold(self):
		url='http://finance.naver.com/sise/item_gold.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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

				value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9]
				cursor.execute("insert into stok0003 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response


	def item_gap(self):
		url='http://finance.naver.com/sise/item_gap.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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

				value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9]
				cursor.execute("insert into stok0004 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response


	def item_igyuk(self):
		url='http://finance.naver.com/sise/item_igyuk.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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

				value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9]
				cursor.execute("insert into stok0005 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def item_overheating_1(self):
		url='http://finance.naver.com/sise/item_overheating_1.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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

				value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9]
				cursor.execute("insert into stok0006 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response


	def item_overheating_2(self):
		url='http://finance.naver.com/sise/item_overheating_2.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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

				value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9]
				cursor.execute("insert into stok0007 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def sise_foreign_hold(self):
		url='http://finance.naver.com/sise/sise_foreign_hold.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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


				value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8]
				cursor.execute("insert into stok0008 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response


	def sise_quant_0(self):
		url='http://finance.naver.com/sise/sise_quant.nhn?sosok=0'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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

				value=[dao.yyyymmdd(),'00',no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10]
				cursor.execute("insert into stok0009 (base_dt,market,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),'00',no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def sise_quant_1(self):
		url='http://finance.naver.com/sise/sise_quant.nhn?sosok=1'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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

				value=[dao.yyyymmdd(),'01',no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10]
				cursor.execute("insert into stok0009 (base_dt,market,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),'01',no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def sise_upper(self):
		url='http://finance.naver.com/sise/sise_upper.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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

				value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10]
				cursor.execute("insert into stok0010 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def sise_lower(self):
		url='http://finance.naver.com/sise/sise_lower.nhn'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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

				value=[dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10]
				cursor.execute("insert into stok0011 (base_dt,no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),no,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response


	def sise_upjong_t(self):
		url='http://sise.wownet.co.kr/nude/sise/stockPlus.asp?bcode=N02011000&mseq=1531&gubun=T'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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

				value=[dao.yyyymmdd(),title,number1,number2,number3,number4,number5,number6,number7,number8]
				cursor.execute("insert into stok0012 (base_dt,title,number1,number2,number3,number4,number5,number6,number7,number8) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),title,number1,number2,number3,number4,number5,number6,number7,number8))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def sise_upjong_k(self):
		url='http://sise.wownet.co.kr/nude/sise/stockPlus.asp?bcode=N02011000&mseq=1531&gubun=K'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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
				value=[dao.yyyymmdd(),title,number1,number2,number3,number4,number5,number6,number7,number8]
				cursor.execute("insert into stok0013 (base_dt,title,number1,number2,number3,number4,number5,number6,number7,number8) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),title,number1,number2,number3,number4,number5,number6,number7,number8))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def ipo_chyounggu(self):
		url='http://www.ipo38.co.kr/ipo/index.htm?key=1'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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


				value=[dao.yyyymmdd(),basedt,title,status,price,number1,number2,number3,upjgong]
				cursor.execute("insert into stok0014 (base_dt,basedt,title,status,price,number1,number2,number3,upjgong) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),basedt,title,status,price,number1,number2,number3,upjgong))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def ipo_permission(self):
		url='http://www.ipo38.co.kr/ipo/index.htm?key=2'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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


				value=[dao.yyyymmdd(),basedt,title,status,price,number1,number2,number3,upjgong]
				cursor.execute("insert into stok0015 (base_dt,basedt,title,status,price,number1,number2,number3,upjgong) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),basedt,title,status,price,number1,number2,number3,upjgong))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def ipo_ir(self):
		url='http://www.ipo38.co.kr/ipo/index.htm?key=3'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('tr')[25:] :

			if len(content.findAll('td')) == 5 :
				title=content.findAll('td')[0].text.encode('utf-8')
				basedt=content.findAll('td')[1].text.encode('utf-8')
				addr=content.findAll('td')[2].text.encode('utf-8').replace('&nbsp;','')
				price=content.findAll('td')[3].text.encode('utf-8')
				enterprise=content.findAll('td')[4].text.encode('utf-8')

				value=[dao.yyyymmdd(),title,basedt,addr,price,enterprise]

				cursor.execute("insert into stok0016 (base_dt,title,basedt,addr,price,enterprise) values (%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),title,basedt,addr,price,enterprise))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def ipo_suyo_predict(self):
		url='http://www.ipo38.co.kr/ipo/index.htm?key=4'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('tr')[25:] :

			if len(content.findAll('td')) == 6:
				title=content.findAll('td')[0].text.encode('utf-8').replace('&nbsp;','')
				basedt=content.findAll('td')[1].text.encode('utf-8')
				want_gongmoga=content.findAll('td')[2].text.encode('utf-8').replace('&nbsp;','')
				fix_gongmoga=content.findAll('td')[3].text.encode('utf-8')
				total_gongmoga=content.findAll('td')[4].text.encode('utf-8')
				enterprise=content.findAll('td')[5].text.encode('utf-8')

				value=[dao.yyyymmdd(),title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,enterprise]
				cursor.execute("insert into stok0017 (base_dt,title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,enterprise) values (%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,enterprise))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response
	def ipo_suyo_result(self):
		url='http://www.ipo38.co.kr/ipo/index.htm?key=5'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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


				value=[dao.yyyymmdd(),title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,competetion,percent,enterprise]
				cursor.execute("insert into stok0018 (base_dt,title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,competetion,percent,enterprise) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,competetion,percent,enterprise))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response
	def ipo_gongmo(self):
		url='http://www.ipo38.co.kr/ipo/index.htm?key=6'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('tr')[25:] :

			if len(content.findAll('td')) == 7 and len(content.findAll('table')) == 0:

				title=content.findAll('td')[0].text.encode('utf-8').replace('&nbsp;','')
				basedt=content.findAll('td')[1].text.encode('utf-8')
				want_gongmoga=content.findAll('td')[2].text.encode('utf-8')
				fix_gongmoga=content.findAll('td')[3].text.encode('utf-8')
				total_gongmoga=content.findAll('td')[4].text.encode('utf-8')
				competetion=content.findAll('td')[5].text.encode('utf-8')

				enterprise=content.findAll('td')[6].text.encode('utf-8')


				value=[dao.yyyymmdd(),title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,competetion,enterprise]
				cursor.execute("insert into stok0019 (base_dt,title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,competetion,enterprise) values (%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),title,basedt,want_gongmoga,fix_gongmoga,total_gongmoga,competetion,enterprise))
		mysql.commit()
		cursor.close()
		mysql.close()

		return response
	def ipo_new(self):
		url='http://www.ipo38.co.kr/ipo/index.htm?key=7'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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

				value=[dao.yyyymmdd(),title,basedt,number1,number2,number3,number4,number5,number6,number7,number8]
				cursor.execute("insert into stok0020 (base_dt,title,basedt,number1,number2,number3,number4,number5,number6,number7,number8) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),title,basedt,number1,number2,number3,number4,number5,number6,number7,number8))
		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def ipo_cbbw(self):
		url='http://www.ipo38.co.kr/fund/'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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


				value=[dao.yyyymmdd(),mk_dscd,basedt,title,number2,number3,number4,number5,enterprise,event_dt]
				cursor.execute("insert into stok0021 (base_dt,dscd,basedt,title,number2,number3,number4,number5,enterprise,event_dt) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),mk_dscd,basedt,title,number2,number3,number4,number5,enterprise,event_dt))
		mysql.commit()
		cursor.close()
		mysql.close()

		return response


	def ipo_ilban(self):
		url='http://www.ipo38.co.kr/fund1/'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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

				value=[dao.yyyymmdd(),title,mk_dscd,basedt,number2,number3,number4,number5,number6,enterprise]
				cursor.execute("insert into stok0022 (base_dt,title,dscd,basedt,number2,number3,number4,number5,number6,enterprise) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),title,mk_dscd,basedt,number2,number3,number4,number5,number6,enterprise))
		mysql.commit()
		cursor.close()
		mysql.close()

		return response



	def munji(self):
		url='http://cleanair.seoul.go.kr/air_city.htm?method=measure&grp1=pm10'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
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

			value=[dao.yyyymmdd(),title,mise,chomise,ozone,esan,ilsan,awhang,grade,jisu,material]
			cursor.execute("insert into news0003 (base_dt,title,mise,chomise,ozone,esan,ilsan,awhang,grade,jisu,material) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),title,mise,chomise,ozone,esan,ilsan,awhang,grade,jisu,material))
		mysql.commit()
		cursor.close()
		mysql.close()

		return response



	def sise_group(self):
		url='http://finance.naver.com/sise/sise_group.nhn?type=group'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('tr')[1:] :
			if len(content.findAll('td')) == 7 and len(content.findAll('th')) ==0:
				title=content.findAll('td')[0].text.encode('utf-8')
				number1=content.findAll('td')[1].text.encode('utf-8')
				number2=content.findAll('td')[2].text.encode('utf-8')
				number3=content.findAll('td')[3].text.encode('utf-8')
				number4=content.findAll('td')[4].text.encode('utf-8')
				number5=content.findAll('td')[5].text.encode('utf-8')

				value=[dao.yyyymmdd(),title,number1,number2,number3,number4,number5]
				cursor.execute("insert into stok0023 (base_dt,title,number1,number2,number3,number4,number5) values (%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),title,number1,number2,number3,number4,number5))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response








	def jemu_year(self,shcode):
		url='http://www.sejongdata.com/business_include_fr/table_main0_bus_01.html?&no='+shcode+'&gubun=2'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		cnt=0
		for content in soup.findAll('table') :

			if len(content.findAll('tr')) ==  8 or  len(content.findAll('tr')) == 11 :
				content=content.findAll('tr')
				content=BeautifulSoup.BeautifulSoup(str(content))
				for content in content.findAll('tr') :
					cnt=cnt+1
					title=content.findAll('td')[0].text.encode('utf-8')
					number1=content.findAll('td')[1].text.encode('utf-8')
					number2=content.findAll('td')[2].text.encode('utf-8')
					number3=content.findAll('td')[3].text.encode('utf-8')
					number4=content.findAll('td')[4].text.encode('utf-8')
					number5=content.findAll('td')[5].text.encode('utf-8')
					number6=content.findAll('td')[6].text.encode('utf-8')
					number7=content.findAll('td')[7].text.encode('utf-8')
					number8=content.findAll('td')[8].text.encode('utf-8')
					number9=content.findAll('td')[9].text.encode('utf-8')
					number10=content.findAll('td')[10].text.encode('utf-8')

					value=[dao.yyyymmdd(),shcode,cnt,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10]
					cursor.execute("insert into stok0024 (base_dt,shcode,rownum,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),shcode,cnt,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response


	def jemu_month(self,shcode):
		url='http://www.sejongdata.com/business_include_fr/table_main0_bus_02.html?&no='+shcode
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		cnt=0
		for content in soup.findAll('table') [:-4]:

			if len(content.findAll('tr')) ==  7 or len(content.findAll('tr')) ==3 :

				content=content.findAll('tr')
				content=BeautifulSoup.BeautifulSoup(str(content))

				for content in content.findAll('tr') :
					cnt=cnt+1
					title=content.findAll('td')[0].text.encode('utf-8')
					number1=content.findAll('td')[1].text.encode('utf-8')
					number2=content.findAll('td')[2].text.encode('utf-8')
					number3=content.findAll('td')[3].text.encode('utf-8')
					number4=content.findAll('td')[4].text.encode('utf-8')
					number5=content.findAll('td')[5].text.encode('utf-8')
					number6=content.findAll('td')[6].text.encode('utf-8')
					number7=content.findAll('td')[7].text.encode('utf-8')
					number8=content.findAll('td')[8].text.encode('utf-8')
					number9=content.findAll('td')[9].text.encode('utf-8')
					number10=content.findAll('td')[10].text.encode('utf-8')
					number11=content.findAll('td')[11].text.encode('utf-8')
					number12=content.findAll('td')[12].text.encode('utf-8')

					value=[dao.yyyymmdd(),shcode,cnt,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10,number11,number12]
					cursor.execute("insert into stok0025 (base_dt,shcode,rownum,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10,number11,number12) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),shcode,cnt,title,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10,number11,number12))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def abroad_jisu(self):
		url='http://m.finance.daum.net/m/world/index.daum?type=default'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		cnt=0
		for content in soup.findAll('table') :

				for content in content.findAll('tr') :
					# title=content.findAll('td')[0].text.encode('utf-8')
					title=content.findAll('th')[0].text.encode('utf-8')
					number1=content.findAll('td')[0].text.encode('utf-8')
					number2=content.findAll('td')[1].text.encode('utf-8')
					number3=content.findAll('td')[2].text.encode('utf-8')

					value=[dao.yyyymmdd(),title,number1,number2,number3]
					cursor.execute("insert into stok0026 (base_dt,title,number1,number2,number3) values (%s,%s,%s,%s,%s)",(dao.yyyymmdd(),title,number1,number2,number3))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response


	def present_jisu(self):
		url='http://m.finance.daum.net/m/world/market.daum?type=cm'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		cnt=0
		for content in soup.findAll('table') :

				for content in content.findAll('tr') :
					# title=content.findAll('td')[0].text.encode('utf-8')
					title=content.findAll('th')[0].text.encode('utf-8')
					number1=content.findAll('td')[0].text.encode('utf-8')
					number2=content.findAll('td')[1].text.encode('utf-8')
					number3=content.findAll('td')[2].text.encode('utf-8')

					value=[dao.yyyymmdd(),title,number1,number2,number3]
					cursor.execute("insert into stok0027 (base_dt,title,number1,number2,number3) values (%s,%s,%s,%s,%s)",(dao.yyyymmdd(),title,number1,number2,number3))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def etf(self):
		url='http://vip.mk.co.kr/newSt/price/etf.php'
		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader)
		soup = BeautifulSoup.BeautifulSoup(r.content)
		# soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('table') [0:1]:
			for content in content.findAll('tr') :
				if len(content.findAll('td')) ==7:
					title=content.findAll('td')[0].text.encode('utf-8')
					number1=content.findAll('td')[1].text.encode('utf-8')
					number2=content.findAll('td')[2].text.encode('utf-8')
					number3=content.findAll('td')[3].text.encode('utf-8')
					number4=content.findAll('td')[4].text.encode('utf-8')
					number5=content.findAll('td')[5].text.encode('utf-8')
					number6=content.findAll('td')[6].text.encode('utf-8')

					value=[dao.yyyymmdd(),title,number1,number2,number3,number4,number5,number6]
					cursor.execute("insert into stok0028 (base_dt,title,number1,number2,number3,number4,number5,number6) values (%s,%s,%s,%s,%s,%s,%s,%s)",(dao.yyyymmdd(),title,number1,number2,number3,number4,number5,number6))

		mysql.commit()
		cursor.close()
		mysql.close()

		return response










































































########################################################################################################3

	def t8430(self):
		pythoncom.CoInitialize()
		server_addr = self.server_addr
		server_port = self.server_port
		server_type = self.server_type
		user_id = self.user_id
		user_pass = self.user_pass
		user_certificate_pass = self.user_certificate_pass
		response=[]
		#--------------------------------------------------------------------------
		# Login Session
		#--------------------------------------------------------------------------
		inXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEvents)
		inXASession.ConnectServer(server_addr, server_port)
		inXASession.Login(user_id, user_pass, user_certificate_pass, server_type, 0)

		while XASessionEvents.logInState == 0:
		    pythoncom.PumpWaitingMessages()

		inXAQuery = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEvents)
		inXAQuery.LoadFromResFile("C:\\eBEST\\xingAPI\\Res\\t8430.res")
		inXAQuery.SetFieldData('t8430InBlock', 'gubun', 0, 0)
		inXAQuery.Request(0)
		i=0
		while XAQueryEvents.queryState == 0:
		    pythoncom.PumpWaitingMessages()
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		inx = inXAQuery.GetBlockCount('t8430OutBlock')
		for i in range(inx):
			hname = inXAQuery.GetFieldData('t8430OutBlock', 'hname', i).encode("utf-8")
			shcode = inXAQuery.GetFieldData('t8430OutBlock', 'shcode', i).encode("utf-8")
			expcode = inXAQuery.GetFieldData('t8430OutBlock', 'expcode', i).encode("utf-8")
			etfgubun = inXAQuery.GetFieldData('t8430OutBlock', 'etfgubun', i).encode("utf-8")
			uplmtprice = inXAQuery.GetFieldData('t8430OutBlock', 'uplmtprice', i).encode("utf-8")
			dnlmtprice = inXAQuery.GetFieldData('t8430OutBlock', 'dnlmtprice', i).encode("utf-8")
			jnilclose = inXAQuery.GetFieldData('t8430OutBlock', 'jnilclose', i).encode("utf-8")
			memedan = inXAQuery.GetFieldData('t8430OutBlock', 'memedan', i).encode("utf-8")
			recprice = inXAQuery.GetFieldData('t8430OutBlock', 'recprice', i).encode("utf-8")
			gubun = inXAQuery.GetFieldData('t8430OutBlock', 'gubun', i).encode("utf-8")
			print shcode
			cursor.execute('INSERT INTO t8430 values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (dao.yyyymmdd(),hname,shcode,expcode,etfgubun,uplmtprice,dnlmtprice,jnilclose,memedan,recprice,gubun))
		print inx
		mysql.commit()
		cursor.close()
		mysql.close()
		XAQueryEvents.queryState = 0
		XASessionEvents.logInState = 0
		return response


	def shcode(self):
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		dao=db.db()
		result=[]
		response=[]
		rp =dao.select('select shcode from t8430  ')
		return rp










































































































































































































####################################################################################################################33
	def sbs_news(self,category):
		url=""
		if category =='00':
			url='http://api.sbs.co.kr/xml/news/rss.jsp?pmDiv=external'
		elif 	category =='01':
			url='http://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=01'
		elif 	category =='02':
			url='http://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=02'
		elif 	category =='03':
			url='http://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=03'
		elif 	category =='04':
			url='http://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=14'
		elif 	category =='05':
			url='http://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=07'
		elif 	category =='06':
			url='http://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=09'
		elif 	category =='07':
			url='http://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=08'
		elif 	category =='08':
			url='http://api.sbs.co.kr/xml/news/rss.jsp?pmDiv=8news'
		elif 	category =='09':
			url='http://api.sbs.co.kr/xml/news/rss.jsp?pmDiv=morning_news'
		elif 	category =='10':
			url='http://news.sbs.co.kr/news/VideoMug_RssFeed.do'
		elif 	category =='11':
			url='http://api.sbs.co.kr/xml/news/rss.jsp?pmDiv=ranking'
		elif 	category =='12':
			url='http://news.sbs.co.kr/news/Special_RssFeed.do'
		elif 	category =='13':
			url='http://api.sbs.co.kr/xml/news/rss.jsp?pmDiv=vod_talk'

		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).text
		#soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

		 	title= content.find('title').text.encode('utf-8')
		 	link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			author= content.find('author').text.encode('utf-8')
			category= content.find('category').text.encode('utf-8')
			guid= content.find('guid').text.encode('utf-8')
			pubdate= content.find('pubdate').text.encode('utf-8')

			image=''
			try:
				value=['sbs',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , ('sbs',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"

		mysql.commit()
		cursor.close()
		mysql.close()


		return response

	def mbc_news(self,category):
		if category =='00':
			url='http://imnews.imbc.com/rss/news/news_00.xml'
		elif 	category =='01':
			url='http://imnews.imbc.com/rss/news/news_01.xml'
		elif 	category =='01':
			url='http://imnews.imbc.com/rss/news/news_03.xml'
		elif 	category =='01':
			url='http://imnews.imbc.com/rss/news/news_04.xml'
		elif 	category =='01':
			url='http://imnews.imbc.com/rss/news/news_05.xml'
		elif 	category =='01':
			url='http://imnews.imbc.com/rss/news/news_06.xml'
		elif 	category =='01':
			url='http://imnews.imbc.com/rss/news/news_07.xml'

		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			author= content.find('author').text.encode('utf-8')
			if content.find('category') != None :
				category= content.find('category').text.encode('utf-8')
			else:
				category=''
			guid= ''
			pubdate= content.find('pubdate').text.encode('utf-8')
			image=''
			try:
				value=['mbc',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('mbc',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"

		mysql.commit()
		cursor.close()
		mysql.close()


		return response


	def chosun_news(self,category):
		if category =='00':
			url='http://www.chosun.com/site/data/rss/rss.xml'
		elif 	category =='01':
			url='http://myhome.chosun.com/rss/www_section_rss.xml'
		elif 	category =='02':
			url='http://www.chosun.com/site/data/rss/politics.xml'
		elif 	category =='03':
			url='http://www.chosun.com/site/data/rss/international.xml'
		elif 	category =='04':
			url='http://www.chosun.com/site/data/rss/culture.xml'
		elif 	category =='05':
			url='http://www.chosun.com/site/data/rss/editorials.xml'
		elif 	category =='06':
			url='http://www.chosun.com/site/data/rss/video.xml'
		elif 	category =='07':
			url='http://inside.chosun.com/rss/rss.xml'
		elif 	category =='08':
			url='http://photo.chosun.com/site/data/rss/photonews.xml'
		elif 	category =='09':
			url='http://newsplus.chosun.com/hitdata/xml/index/index.xml'

		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			author= content.find('author').text.encode('utf-8')
			category= content.find('category').text.encode('utf-8')
			guid= ''
			pubdate= content.find('pubdate').text.encode('utf-8')
			image=''


			try:
				value=['chosun',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('chosun',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"
		mysql.commit()
		cursor.close()
		mysql.close()




		return response

	def chosun_biz(self,category):
		if category =='00':
			url='http://biz.chosun.com/site/data/rss/rss.xml'
		elif 	category =='01':
			url='http://biz.chosun.com/site/data/rss/news.xml'
		elif 	category =='02':
			url='http://biz.chosun.com/site/data/rss/market.xml'
		elif 	category =='03':
			url='http://biz.chosun.com/site/data/rss/policybank.xml'
		elif 	category =='04':
			url='http://biz.chosun.com/site/data/rss/estate.xml'
		elif 	category =='05':
			url='ttp://biz.chosun.com/site/data/rss/enterprise.xml'
		elif 	category =='06':
			url='http://biz.chosun.com/site/data/rss/global.xml'
		elif 	category =='07':
			url='http://biz.chosun.com/site/data/rss/weeklybiz.xml'
		elif 	category =='08':
			url='http://newsplus.chosun.com/hitdata/xml/chosunbiz/index/index.xml'


		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			author= content.find('author').text.encode('utf-8')
			category= content.find('category').text.encode('utf-8')
			guid= ''
			pubdate= content.find('pubdate').text.encode('utf-8')
			image=''
			try:
				value=['chosun_biz',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('chosun_biz',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"
		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def chosun_ent(self,category):
		if category =='00':
			url='http://www.chosun.com/site/data/rss/sports.xml'
		elif 	category =='01':
			url='http://www.chosun.com/site/data/rss/ent.xml'
		elif 	category =='02':
			url='http://thestar.chosun.com/site/data/rss/rss.xml'
		elif 	category =='03':
			url='http://keywui.chosun.com/rss/rss.xml'
		elif 	category =='04':
			url='http://newsplus.chosun.com/hitdata/xml/se/sports/index.xml'
		elif 	category =='05':
			url='http://newsplus.chosun.com/hitdata/xml/se/star/index.xml'

		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			author= content.find('author').text.encode('utf-8')
			category= content.find('category').text.encode('utf-8')
			guid= ''
			pubdate= content.find('pubdate').text.encode('utf-8')
			image=''
			try:
				value=['chosun_ent',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('chosun_ent',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"

		mysql.commit()
		cursor.close()
		mysql.close()


		return response


	def chosun_newsplus(self,category):
		if category =='00':
			url='http://newsplus.chosun.com/site/data/rss/news.xml'
		elif 	category =='01':
			url='http://newsplus.chosun.com/inside/xml/inside_rss.xml'
		elif 	category =='02':
			url='http://danmee.chosun.com/site/data/rss/rss.xml'
		elif 	category =='03':
			url='http://health.chosun.com/site/data/rss/rss.xml'
		elif 	category =='04':
			url='http://careview.chosun.com/site/data/rss/rss.xml'
		elif 	category =='05':
			url='http://travel.chosun.com/site/data/rss/rss.xml'
		elif 	category =='06':
			url='http://review.chosun.com/site/data/rss/rss.xml'
		elif 	category =='07':
			url='http://books.chosun.com/site/data/rss/rss.xml'
		elif 	category =='08':
			url='http://art.chosun.com/site/data/rss/rss.xml'
		elif 	category =='09':
			url='http://myhome.chosun.com/rss/kid_section_rss.xml'
		elif 	category =='10':
			url='http://health.chosun.com/rss/column.xml'
		elif 	category =='11':
			url='http://newsplus.chosun.com/hitdata/xml/newsplus/index/index.xml'

		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			author= content.find('author').text.encode('utf-8')
			category= content.find('category').text.encode('utf-8')
			guid= ''
			pubdate= content.find('pubdate').text.encode('utf-8')
			image=''

			try:
				value=['chosun_newsplus',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('chosun_newsplus',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"
		mysql.commit()
		cursor.close()
		mysql.close()


		return response


	def joins_news(self,category):
		if category =='00':
			url='http://rss.joins.com/joins_news_list.xml'
		elif 	category =='01':
			url='http://rss.joins.com/joins_money_list.xml'
		elif 	category =='02':
			url='http://rss.joins.com/joins_topic_list.xml'
		elif 	category =='03':
			url='http://rss.joins.com/joins_sports_list.xml'
		elif 	category =='04':
			url='http://rss.joins.com/joins_star_list.xml'
		elif 	category =='05':
			url='http://rss.joins.com/joins_life_list.xml'
		elif 	category =='06':
			url='http://rss.joins.com/joins_politics_list.xml'
		elif 	category =='07':
			url='http://rss.joins.com/joins_world_list.xml'
		elif 	category =='08':
			url='http://rss.joins.com/joins_it_list.xml'
		elif 	category =='09':
			url='http://rss.joins.com/joins_opinion_list.xml'


		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			author= content.find('author').text.encode('utf-8')
			category= ''
			guid= ''
			pubdate= content.find('pubdate').text.encode('utf-8')
			image=''
			try:
				value=['joins_news',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('joins_news',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"
		mysql.commit()
		cursor.close()
		mysql.close()

		return response



	def nocut_news(self,category):
		if category =='00':
			url='http://rss.nocutnews.co.kr/nocutnews.xml'
		elif 	category =='01':
			url='http://rss.nocutnews.co.kr/NocutPolitics.xml'
		elif 	category =='02':
			url='http://rss.nocutnews.co.kr/NocutSocial.xml'
		elif 	category =='03':
			url='http://rss.nocutnews.co.kr/NocutEconomy.xml'
		elif 	category =='04':
			url='http://rss.nocutnews.co.kr/NocutIndustry.xml'
		elif 	category =='05':
			url='http://rss.nocutnews.co.kr/NocutSports.xml'
		elif 	category =='06':
			url='http://rss.nocutnews.co.kr/NocutLocal.xml'
		elif 	category =='07':
			url='http://rss.nocutnews.co.kr/NocutGlobal.xml'
		elif 	category =='08':
			url='http://rss.nocutnews.co.kr/NocutIT.xml'
		elif 	category =='09':
			url='http://rss.nocutnews.co.kr/NocutEnter.xml'
		elif 	category =='10':
			url='http://rss.nocutnews.co.kr/NocutCulture.xml'
		elif 	category =='11':
			url='http://rss.nocutnews.co.kr/NocutPhoto.xml'
		elif 	category =='12':
			url='http://rss.nocutnews.co.kr/NocutColum.xml'
		elif 	category =='13':
			url='http://rss.nocutnews.co.kr/NocutEtc.xml'
		elif 	category =='14':
			url='http://rss.nocutnews.co.kr/NocutOnly.xml'
		elif 	category =='15':
			url='http://rss.nocutnews.co.kr/NocutHotissue.xml'
		elif 	category =='16':
			url='http://rss.nocutnews.co.kr/NocutCplan.xml'

		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			image= content.find('image').text.encode('utf-8')
			author= ''
			category= ''
			guid= ''
			pubdate= content.find('dc:date').text.encode('utf-8')
			try:
				value=['nocut_news',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('nocut_news',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"

		mysql.commit()
		cursor.close()
		mysql.close()


		return response

	def donga_news(self,category):
		if category =='00':
			url='http://rss.donga.com/total.xml'
		elif 	category =='01':
			url='http://rss.donga.com/politics.xml'
		elif 	category =='02':
			url='http://rss.donga.com/national.xml'
		elif 	category =='03':
			url='http://rss.donga.com/economy.xml'
		elif 	category =='04':
			url='http://rss.donga.com/international.xml'
		elif 	category =='05':
			url='http://rss.donga.com/editorials.xml'
		elif 	category =='06':
			url='http://rss.donga.com/science.xml'
		elif 	category =='07':
			url='http://rss.donga.com/culture.xml'
		elif 	category =='08':
			url='http://rss.donga.com/sports.xml'
		elif 	category =='09':
			url='http://rss.donga.com/inmul.xml'
		elif 	category =='10':
			url='http://rss.donga.com/health.xml'
		elif 	category =='11':
			url='http://rss.donga.com/leisure.xml'
		elif 	category =='12':
			url='http://rss.donga.com/book.xml'
		elif 	category =='13':
			url='http://rss.donga.com/show.xml'
		elif 	category =='14':
			url='http://rss.donga.com/woman.xml'
		elif 	category =='15':
			url='http://rss.donga.com/child.xml'
		elif 	category =='16':
			url='http://rss.donga.com/travel.xml'
		elif 	category =='17':
			url='http://rss.donga.com/lifeinfo.xml'


		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			if content.find('media:content') != None :
				image= content.find('media:content').text.encode('utf-8')
			else:
				image=''
			author= ''
			category= ''
			guid= ''

			pubdate= content.find('pubdate').text.encode('utf-8')


			try:
				value=['donga_news',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('donga_news',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"

		mysql.commit()
		cursor.close()
		mysql.close()


		return response


	def segye_news(self,category):
		if category =='00':
			url='http://rss.segye.com/segye_recent.xml'
		elif 	category =='01':
			url='http://rss.segye.com/segye_total.xml'
		elif 	category =='02':
			url='http://rss.segye.com/segye_politic.xml'
		elif 	category =='03':
			url='http://rss.segye.com/segye_international.xml'
		elif 	category =='04':
			url='http://rss.segye.com/segye_economy.xml'
		elif 	category =='05':
			url='http://rss.segye.com/segye_society.xml'
		elif 	category =='06':
			url='http://rss.segye.com/segye_culture.xml'
		elif 	category =='07':
			url='http://rss.segye.com/segye_sports.xml'
		elif 	category =='08':
			url='http://rss.segye.com/segye_entertainment.xml'
		elif 	category =='09':
			url='http://rss.segye.com/segye_people.xml'
		elif 	category =='10':
			url='http://rss.segye.com/segye_opinion.xml'
		elif 	category =='11':
			url='http://rss.segye.com/segye_local.xml'
		elif 	category =='12':
			url='http://rss.segye.com/segye_task_force.xml'
		elif 	category =='13':
			url='http://rss.segye.com/segye_family.xml'
		elif 	category =='14':
			url='http://rss.segye.com/segye_root.xml'
		elif 	category =='15':
			url='http://rss.segye.com/segye_punchnews.xml'
		elif 	category =='16':
			url='http://rss.segye.com/segye_photo.xml'
		elif 	category =='17':
			url='http://rss.segye.com/segye_segyeTV.xml'


		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			image=''
			author= ''
			category= ''
			guid= content.find('guid').text.encode('utf-8')
			pubdate= content.find('pubdate').text.encode('utf-8')

			try:
				value=['segye_news',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('segye_news',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"
		mysql.commit()
		cursor.close()
		mysql.close()



		return response

	def ohmy_news(self,category):
		if category =='00':
			url='http://rss.ohmynews.com/rss/ohmynews.xml'
		elif 	category =='01':
			url='http://rss.ohmynews.com/rss/top.xml'
		elif 	category =='02':
			url='http://rss.ohmynews.com/rss/life.xml'
		elif 	category =='03':
			url='http://rss.ohmynews.com/rss/society.xml'
		elif 	category =='04':
			url='http://rss.ohmynews.com/rss/culture.xml'
		elif 	category =='05':
			url='http://rss.ohmynews.com/rss/politics.xml'
		elif 	category =='06':
			url='http://rss.ohmynews.com/rss/economy.xml'
		elif 	category =='07':
			url='http://rss.ohmynews.com/rss/international.xml'
		elif 	category =='08':
			url='http://rss.ohmynews.com/rss/education.xml'
		elif 	category =='09':
			url='http://rss.ohmynews.com/rss/sports.xml'
		elif 	category =='10':
			url='http://rss.ohmynews.com/rss/cinema.xml'
		elif 	category =='11':
			url='http://rss.ohmynews.com/rss/media.xml'
		elif 	category =='12':
			url='http://rss.ohmynews.com/rss/travel.xml'
		elif 	category =='13':
			url='http://rss.ohmynews.com/rss/book.xml'
		elif 	category =='14':
			url='http://rss.ohmynews.com/rss/woman.xml'
		elif 	category =='15':
			url='http://rss.ohmynews.com/rss/jeolla.xml'
		elif 	category =='16':
			url='http://rss.ohmynews.com/rss/gyeongnam.xml'
		elif 	category =='17':
			url='http://rss.ohmynews.com/rss/chungnam.xml'
		elif 	category =='18':
			url='http://rss.ohmynews.com/rss/gyeonggi.xml'
		elif 	category =='19':
			url='http://rss.ohmynews.com/rss/ab_reporter.xml'
		elif 	category =='20':
			url='http://rss.ohmynews.com/rss/cartoon.xml'

		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			image=''
			author= content.find('author').text.encode('utf-8')
			category= content.find('category').text.encode('utf-8')
			guid= ''
			pubdate= content.find('pubdate').text.encode('utf-8')
			try:
				value=['ohmy_news',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('ohmy_news',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"

		mysql.commit()
		cursor.close()
		mysql.close()


		return response


	def hani_news(self,category):
		if category =='00':
			url='http://www.hani.co.kr/rss/'
		elif 	category =='01':
			url='http://www.hani.co.kr/rss/politics/'
		elif 	category =='02':
			url='http://www.hani.co.kr/rss/economy/'
		elif 	category =='03':
			url='http://www.hani.co.kr/rss/society/'
		elif 	category =='04':
			url='http://www.hani.co.kr/rss/international/'
		elif 	category =='05':
			url='http://www.hani.co.kr/rss/culture/'
		elif 	category =='06':
			url='http://www.hani.co.kr/rss/sports/'
		elif 	category =='07':
			url='http://www.hani.co.kr/rss/science/'
		elif 	category =='08':
			url='http://www.hani.co.kr/rss/opinion/'
		elif 	category =='09':
			url='http://www.hani.co.kr/rss/cartoon/'
		elif 	category =='10':
			url='http://www.hani.co.kr/rss/english_edition/'
		elif 	category =='11':
			url='http://www.hani.co.kr/rss/specialsection/'
		elif 	category =='12':
			url='http://www.hani.co.kr/rss/hanionly/'
		elif 	category =='13':
			url='http://www.hani.co.kr/rss/hkronly/'
		elif 	category =='14':
			url='http://www.hani.co.kr/rss/multihani/'
		elif 	category =='15':
			url='http://www.hani.co.kr/rss/lead/'
		elif 	category =='16':
			url='http://www.hani.co.kr/rss/newsrank/'

		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			image=''
			author= ''
			category= content.find('dc:category').text.encode('utf-8')
			guid= ''
			# subject=content.find('subject').text.encode('utf-8')
			pubdate= content.find('pubdate').text.encode('utf-8')





			try:
				value=['hani_news',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('hani_news',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"

		mysql.commit()
		cursor.close()
		mysql.close()


		return response


	def mk_news(self,category):
		if category =='00':
			url='http://file.mk.co.kr/news/rss/rss_30000001.xml'
		elif 	category =='01':
			url='http://file.mk.co.kr/news/rss/rss_30000023.xml'
		elif 	category =='02':
			url='http://file.mk.co.kr/news/rss/rss_40300001.xml'
		elif 	category =='03':
			url='http://file.mk.co.kr/news/rss/rss_50600001.xml'
		elif 	category =='04':
			url='http://file.mk.co.kr/news/rss/rss_30100041.xml'
		elif 	category =='05':
			url='http://file.mk.co.kr/news/rss/rss_50700001.xml'
		elif 	category =='06':
			url='http://file.mk.co.kr/news/rss/rss_30200030.xml'
		elif 	category =='07':
			url='http://file.mk.co.kr/news/rss/rss_30500041.xml'
		elif 	category =='08':
			url='http://file.mk.co.kr/news/rss/rss_50400012.xml'
		elif 	category =='09':
			url='http://file.mk.co.kr/news/rss/rss_30300018.xml'
		elif 	category =='10':
			url='http://file.mk.co.kr/news/rss/rss_50100032.xml'
		elif 	category =='11':
			url='http://file.mk.co.kr/news/rss/rss_50200011.xml'
		elif 	category =='12':
			url='http://file.mk.co.kr/news/rss/rss_50300009.xml'
		elif 	category =='13':
			url='http://file.mk.co.kr/news/rss/rss_40200124.xml'
		elif 	category =='14':
			url='http://file.mk.co.kr/news/rss/rss_40200003.xml'
		elif 	category =='15':
			url='http://file.mk.co.kr/news/rss/rss_30800011.xml'
		elif 	category =='16':
			url='http://file.mk.co.kr/news/rss/rss_50000001.xml'
		elif 	category =='17':
			url='http://file.mk.co.kr/news/rss/rss_60000007.xml'

		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			image=''
			author= content.find('author').text.encode('utf-8')
			category= content.find('category').text.encode('utf-8')
			guid= content.find('no').text.encode('utf-8')
			# subject=content.find('subject').text.encode('utf-8')
			pubdate= content.find('pubdate').text.encode('utf-8')


			try:
				value=['mk_news',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('mk_news',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"
		mysql.commit()
		cursor.close()
		mysql.close()


		return response


	def khan_news(self,category):
		if category =='00':
			url='http://www.khan.co.kr/rss/rssdata/total_news.xml'
		elif 	category =='01':
			url='http://www.khan.co.kr/rss/rssdata/opinion.xml'
		elif 	category =='02':
			url='http://www.khan.co.kr/rss/rssdata/politic.xml'
		elif 	category =='03':
			url='http://www.khan.co.kr/rss/rssdata/economy.xml'
		elif 	category =='04':
			url='http://www.khan.co.kr/rss/rssdata/society.xml'
		elif 	category =='05':
			url='http://www.khan.co.kr/rss/rssdata/culture.xml'
		elif 	category =='06':
			url='http://www.khan.co.kr/rss/rssdata/itnews.xml'
		elif 	category =='07':
			url='http://www.khan.co.kr/rss/rssdata/world.xml'
		elif 	category =='08':
			url='http://www.khan.co.kr/rss/rssdata/sports.xml'
		elif 	category =='09':
			url='http://www.khan.co.kr/rss/rssdata/mx.xml'
		elif 	category =='10':
			url='http://www.khan.co.kr/rss/rssdata/people.xml'
		elif 	category =='11':
			url='http://www.khan.co.kr/rss/rssdata/kh_sports.xml'
		elif 	category =='12':
			url='http://www.khan.co.kr/rss/rssdata/kh_entertainment.xml'
		elif 	category =='13':
			url='http://www.khan.co.kr/rss/rssdata/kh_fun.xml'
		elif 	category =='14':
			url='http://www.khan.co.kr/rss/rssdata/kh_unse.xml'


		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()

		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			image=''
			author= content.find('author').text.encode('utf-8')
			category= content.find('category').text.encode('utf-8')
			guid= ''
			# subject=content.find('subject').text.encode('utf-8')
			if content.find('dc:date') != None:
				pubdate= content.find('dc:date').text.encode('utf-8')
			else:
				pubdate=''


			try:
				value=['khan_news',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('khan_news',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except :
				a="123445"
		mysql.commit()
		cursor.close()
		mysql.close()
		return response

	def hankooki_news(self,category):
		if category =='00':
			url='http://rss.hankooki.com/daily/dh_main.xml'
		elif 	category =='01':
			url='http://rss.hankooki.com/daily/dh_politics.xml'
		elif 	category =='02':
			url='http://rss.hankooki.com/daily/dh_economy.xml'
		elif 	category =='03':
			url='http://rss.hankooki.com/daily/dh_society.xml'
		elif 	category =='04':
			url='http://rss.hankooki.com/daily/dh_world.xml'
		elif 	category =='05':
			url='http://rss.hankooki.com/daily/dh_it_tech.xml'
		elif 	category =='06':
			url='http://rss.hankooki.com/daily/dh_culture.xml'
		elif 	category =='07':
			url='http://rss.hankooki.com/daily/dh_life.xml'
		elif 	category =='08':
			url='http://rss.hankooki.com/daily/dh_column.xml'
		elif 	category =='09':
			url='http://rss.hankooki.com/daily/dh_series.xml'
		elif 	category =='10':
			url='http://rss.hankooki.com/daily/dh_biz.xml'

		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			image=''
			author=''
			category=''
			guid= ''

			pubdate= content.find('pubdate').text.encode('utf-8')


			try:
				value=['hankooki_news',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('hankooki_news',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"

		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def sk_news(self,category):
		if category =='00':
			url='http://rss.hankooki.com/economy/sk_main.xml'
		elif 	category =='01':
			url='http://rss.hankooki.com/economy/sk_economy.xml'
		elif 	category =='02':
			url='http://rss.hankooki.com/economy/sk_stock.xml'
		elif 	category =='03':
			url='http://rss.hankooki.com/economy/sk_estate.xml'
		elif 	category =='04':
			url='http://rss.hankooki.com/economy/sk_industry.xml'
		elif 	category =='05':
			url='http://rss.hankooki.com/economy/sk_world.xml'
		elif 	category =='06':
			url='http://rss.hankooki.com/economy/sk_politics.xml'
		elif 	category =='07':
			url='http://rss.hankooki.com/economy/sk_society.xml'
		elif 	category =='08':
			url='http://rss.hankooki.com/economy/sk_culture.xml'
		elif 	category =='09':
			url='http://rss.hankooki.com/economy/sk_opinion.xml'

		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			image=''
			author=''
			category=''
			guid= ''

			pubdate= content.find('pubdate').text.encode('utf-8')
			try:
				value=['sk_news',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('sk_news',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"

		mysql.commit()
		cursor.close()
		mysql.close()


		return response

	def edaily_news(self,category):
		if category =='00':
			url='http://rss.edaily.co.kr/edaily_news.xml'
		elif 	category =='01':
			url='http://rss.edaily.co.kr/stock_news.xml'
		elif 	category =='02':
			url='http://rss.edaily.co.kr/economy_news.xml'
		elif 	category =='03':
			url='http://rss.edaily.co.kr/finance_news.xml'
		elif 	category =='04':
			url='http://rss.edaily.co.kr/bondfx_news.xml'
		elif 	category =='05':
			url='http://rss.edaily.co.kr/enterprise_news.xml'
		elif 	category =='06':
			url='http://rss.edaily.co.kr/world_news.xml'
		elif 	category =='07':
			url='http://rss.edaily.co.kr/realestate_news.xml'
		elif 	category =='08':
			url=' http://rss.edaily.co.kr/happypot_news.xml'
		elif 	category =='09':
			url='http://rss.edaily.co.kr/edaily_column.xml'
		elif 	category =='10':
			url='http://rss.edaily.co.kr/efn_news.xml'

		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			image=''
			author=''
			category=''
			guid= content.find('guid').text.encode('utf-8')

			pubdate= content.find('pubdate').text.encode('utf-8')


			try:
				value=['edaily_news',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('edaily_news',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"
		mysql.commit()
		cursor.close()
		mysql.close()

		return response


	def mt_news(self,category):
		if category =='00':
			url='http://rss.mt.co.kr/mt_news.xml'
		elif 	category =='01':
			url='http://rss.mt.co.kr/st_news.xml'
		elif 	category =='02':
			url='http://rss.mt.co.kr/mt_column.xml'
		elif 	category =='03':
			url='http://rss.mt.co.kr/biz_news.xml'
		elif 	category =='04':
			url='http://rss.mt.co.kr/coolmoney_news.xml'
		elif 	category =='05':
			url='http://rss.mt.co.kr/stylem_news.xml'
		elif 	category =='06':
			url='http://rss.mt.co.kr/osen_news.xml'

		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			image=''
			author=''
			category=''
			guid= ''

			pubdate= content.find('pubdate').text.encode('utf-8')

			try:
				value=['mt_news',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('mt_news',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"
		mysql.commit()
		cursor.close()
		mysql.close()

		return response

	def hankyung_news(self,category):
		if category =='00':
			url='http://rss.hankyung.com/new/news_main.xml'
		elif 	category =='01':
			url='http://rss.hankyung.com/new/news_stock.xml'
		elif 	category =='02':
			url='http://rss.hankyung.com/new/news_economy.xml'
		elif 	category =='03':
			url='http://rss.hankyung.com/new/news_industry.xml'
		elif 	category =='04':
			url='http://rss.hankyung.com/new/news_estate.xml'
		elif 	category =='05':
			url='http://rss.hankyung.com/new/news_politics.xml'
		elif 	category =='06':
			url='http://rss.hankyung.com/new/news_society.xml'
		elif 	category =='07':
			url='http://rss.hankyung.com/new/news_sports.xml'
		elif 	category =='08':
			url='http://rss.hankyung.com/new/news_enter.xml'
		elif 	category =='09':
			url='http://rss.hankyung.com/new/news_photo.xml'
		elif 	category =='10':
			url='http://rss.hankyung.com/new/column_all.xml'
		elif 	category =='11':
			url='http://rss.hankyung.com/new/column_stock.xml'
		elif 	category =='12':
			url='http://rss.hankyung.com/new/column_land.xml'
		elif 	category =='13':
			url='http://rss.hankyung.com/new/column_ft.xml'
		elif 	category =='14':
			url='http://rss.hankyung.com/new/column_auto.xml'
		elif 	category =='15':
			url='http://rss.hankyung.com/new/column_golf.xml'
		elif 	category =='16':
			url='http://rss.hankyung.com/new/column_community.xml'
		elif 	category =='17':
			url='http://rss.hankyung.com/new/column_english.xml'

		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			image=''
			author=content.find('author').text.encode('utf-8')
			category=''
			guid= ''

			pubdate= content.find('pubdate').text.encode('utf-8')

			try:
				value=['hankyung_news',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('hankyung_news',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"

		mysql.commit()
		cursor.close()
		mysql.close()


		return response

	def fn_news(self,category,search_date):
		if category =='00':
			url='http://www.fnnews.com/rss/new/fn_realnews_all.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='01':
			url='http://www.fnnews.com/rss/new/fn_realnews_politics.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='02':
			url='http://www.fnnews.com/rss/new/fn_realnews_international.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='03':
			url='http://www.fnnews.com/rss/new/fn_realnews_society.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='04':
			url='http://www.fnnews.com/rss/new/fn_realnews_edu.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='05':
			url='http://www.fnnews.com/rss/new/fn_realnews_people.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='06':
			url='http://www.fnnews.com/rss/new/fn_realnews_economy.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='07':
			url='http://www.fnnews.com/rss/new/fn_realnews_stock.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='08':
			url='http://www.fnnews.com/rss/new/fn_realnews_finance.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='09':
			url='http://www.fnnews.com/rss/new/fn_realnews_realestate.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='10':
			url='http://www.fnnews.com/rss/new/fn_realnews_industry.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='11':
			url='http://www.fnnews.com/rss/new/fn_realnews_it.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='12':
			url='http://www.fnnews.com/rss/new/fn_realnews_medical.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='13':
			url='http://www.fnnews.com/rss/new/fn_realnews_circulation.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='14':
			url='http://www.fnnews.com/rss/new/fn_realnews_column.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='15':
			url='http://www.fnnews.com/rss/new/fn_realnews_outcolumn.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='16':
			url='http://www.fnnews.com/rss/new/fn_realnews_ent.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='17':
			url='http://www.fnnews.com/rss/new/fn_realnews_sports.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='18':
			url='http://www.fnnews.com/rss/new/fn_realnews_fasion.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='19':
			url='http://www.fnnews.com/rss/new/fn_realnews_living.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='20':
			url='http://www.fnnews.com/rss/new/fn_realnews_health.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='21':
			url='http://www.fnnews.com/rss/new/fn_realnews_car.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='22':
			url='http://www.fnnews.com/rss/new/fn_realnews_culture.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='23':
			url='http://www.fnnews.com/rss/new/kakaostock.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29'
		elif 	category =='24':
			url='http://www.fnnews.com/rss/new/kakaostock.xml;jsessionid=F6A34BBFB701128C89E11D31BD89ED29?search_date='+search_date

		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		category1 = category
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			if 	category1 =='24':

				title= content.find('title').text.encode('utf-8')
				link= content.find('link_url').text.encode('utf-8')
				description= content.find('body').text.encode('utf-8')
				image= ''
				author=content.find('reporter_name').text.encode('utf-8')
				category=content.find('stock_cd').text.encode('utf-8')
				guid=content.find('id').text.encode('utf-8')

				pubdate= content.find('update_date').text.encode('utf-8')
			else :
				title= content.find('title').text.encode('utf-8')
				link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
				description= content.find('description').text.encode('utf-8')
				image= content.find('media:content').text.encode('utf-8')
				author=content.find('author').text.encode('utf-8')
				category=content.find('atom:category').text.encode('utf-8')
				guid=content.find('guid').text.encode('utf-8')

				pubdate= content.find('atom:published').text.encode('utf-8')
			try:
				value=['fn_news',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('fn_news',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"

		mysql.commit()
		cursor.close()
		mysql.close()


		return response


	def i_news(self,category):
		if category =='00':
			url='http://www.inews24.com/rss/news_inews.xml'
		elif 	category =='01':
			url='http://www.inews24.com/rss/news_it.xml'
		elif 	category =='02':
			url='http://www.inews24.com/rss/news_economy.xml'
		elif 	category =='03':
			url='http://www.inews24.com/rss/news_politics.xml'
		elif 	category =='04':
			url='http://www.inews24.com/rss/news_society.xml'
		elif 	category =='05':
			url='http://www.inews24.com/rss/news_culture.xml'
		elif 	category =='06':
			url='http://www.inews24.com/rss/news_life.xml'
		elif 	category =='07':
			url='http://www.inews24.com/rss/news_joy.xml'
		elif 	category =='08':
			url='http://www.inews24.com/rss/news_enter.xml'
		elif 	category =='09':
			url='http://www.inews24.com/rss/news_sports.xml'
		elif 	category =='10':
			url='http://www.inews24.com/rss/news_game.xml'
		elif 	category =='11':
			url='http://www.inews24.com/rss/news_phototv.xml'
		elif 	category =='12':
			url='http://www.inews24.com/rss/news_opinion.xml'
		elif 	category =='13':
			url='http://www.inews24.com/rss/news_mtalk.xml'


		fakeHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		r=requests.get(url, headers=fakeHeader).content
		# soup = BeautifulSoup.BeautifulSoup(r.content)
		soup = bs4(r, "html.parser")
		result =[]
		response =[]
		dao=db.db()
		mysql = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.mysql,charset='utf8',autocommit=True, use_unicode=True)
		mysql.query("SET NAMES 'utf8';")
		cursor = mysql.cursor()
		for content in soup.findAll('item') :

			title= content.find('title').text.encode('utf-8')
			link= content.find_all(string=re.compile("http"))[0].encode('utf-8')
			description= content.find('description').text.encode('utf-8')
			image=''
			if content.find('author') != None:
				author=content.find('author').text.encode('utf-8')
			else:
				author=''
			category=content.find('category').text.encode('utf-8')
			guid= ''

			pubdate= content.find('pubdate').text.encode('utf-8')
			try:
				value=['i_news',dao.sec(),title,link,description,author,category,guid,pubdate,image]
				cursor.execute("insert into news0000 (news,time ,title ,link ,description ,author,category,guid,pubdate,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,('i_news',dao.sec(),title,link,description,author,category,guid,pubdate,image))
			except:
				a="123445"


		return response