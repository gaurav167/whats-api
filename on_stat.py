from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
#from datetime import datetime

class onlineStatus:
	def __init__(self,labels):
		self.labels = labels
		self.url = "https://web.whatsapp.com/"


	def check_on_status(self):
		driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
		print('opening Whatsapp Web')
		driver.get(self.url)
		time.sleep(10)
		try:
			elem = driver.find_element_by_xpath('//span[contains(text(),"%s")]' %self.labels[0])
			elem.click()
		except:
			driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/header/div[2]/div/span/div[3]/div/span').click()
			time.sleep(1)
			driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/header/div[2]/div/span/div[3]/span/div/ul/li[3]/div').click()
			time.sleep(2)
			elem = driver.find_element_by_xpath('//span[contains(text(),"%s")]' %self.labels[0])
			elem.click()

		time.sleep(5)
		header = driver.find_element_by_id('main').find_element_by_tag_name('header')
		on_stat = False
		print('Listening...')
		f = open('logs.txt','a')
		f.write("\n Start Time : " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		f.close()
		stat = header.find_elements_by_tag_name('div')[1]
		while True:
			try:
				online = stat.find_element_by_xpath('/html/body/div/div/div/div[3]/div/header/div[2]/div[2]/span').text
				if online == "online" or online == "typing...":
					if on_stat == False:
						on_stat = True
						on_info = "\n" + self.labels[0] + " : From : " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
						print('writing...')
						f = open('logs.txt','a')
						f.write(on_info)
						f.close()
			except KeyboardInterrupt:
				print("Exiting")
				driver.quit()
				break
			except:
				if on_stat == True:
					on_stat = False
					on_info = " Till : " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
					print('writing...')
					f = open('logs.txt','a')
					f.write(on_info)
					f.close()
		f = open('logs.txt','a')
		f.write("\n End Time : " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		f.close()

	def check_on_statuses(self):
		#Make connection to WhatsApp web
		drivers = []
		for name in self.labels:
			drivers.append(webdriver.Firefox(executable_path='/usr/local/bin/geckodriver'))
			print("Opening Whatsapp Web...")
			drivers[-1].get(self.url)
			time.sleep(10)
		print("Getting Chats...")
		
		try:
			elems = [driver.find_element_by_xpath('//span[contains(text(),"%s")]' %name) for driver in drivers]
			for elem in elems:
				elem.click()
		except:
			more = [driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/header/div[2]/div/span/div[3]/div/span').click() for driver in drivers]
			archived = [driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/header/div[2]/div/span/div[3]/span/div/ul/li[3]/div').click() for driver in drivers]
			time.sleep(2)
			elems = [driver.find_element_by_xpath('//span[contains(text(),"%s")]' %name) for driver in drivers]
			for elem in elems:
				elem.click()
		# chat = driver.find_element_by_id("pane-side").find_element_by_tag_name('div').find_element_by_tag_name('div').find_element_by_tag_name('div').find_elements_by_tag_name('div')[1]
		# chat.click()
		# input_box.send_keys(Keys.ENTER)
		time.sleep(5)
		headers = [driver.find_element_by_id('main').find_element_by_tag_name('header') for driver in drivers]
		on_stat = [False for driver in drivers]  #Set initial online status to False ,i.e, Not Online
		print("Listening...")
		stats = [header.find_elements_by_tag_name('div')[1] for header in headers]
		while True:
			for stat in stats:
				try:
					online = stat.find_elements_by_tag_name('div')[1].find_element_by_tag_name('span').text
					if online == "online" or online == "typing...":
						if on_stat == False:
							on_stat = True
							on_info = "\n" + name + " : From : " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
							f = open('logs.txt','a')
							f.write(on_info)
							f.close()
				except KeyboardInterrupt:
					print("Exiting")
					[driver.quit() for driver in drivers]
					break
				except:
					if on_stat == True:
						on_stat = False
						on_info = " Till : " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
						f = open('logs.txt','a')
						f.write(on_info)
						f.close()
					pass
obj = onlineStatus(['<INSERT NAME HERE>'])
obj.check_on_status()
