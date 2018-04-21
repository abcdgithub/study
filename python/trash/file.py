import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class file:
	def exchange(self):
		binary = 'C:\download\phantomjs\chromedriver.exe'
		options = webdriver.ChromeOptions()
		options.add_experimental_option("prefs", {
		  "download.default_directory": r"C:\download",
		  "download.prompt_for_download": False,
		  "download.directory_upgrade": True,
		  "safebrowsing.enabled": True
		})
		browser = webdriver.Chrome(binary,chrome_options=options)
		browser.get('https://spot.wooribank.com/pot/Dream?withyou=FXXRT0011')
		search = browser.find_element_by_xpath('//*[@id="frm"]/fieldset/div/span/input')
		search.send_keys(Keys.RETURN)
		time.sleep(5)
		search = browser.find_element_by_xpath('//*[@id="resultArea"]/div[2]/span[1]/a')
		search.send_keys(Keys.RETURN)
		time.sleep(5)
		browser.quit()