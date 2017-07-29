from selenium import webdriver
import time
#from datetime import datetime

class onlineStatus:
	def __init__(self,labels):
		self.labels = labels
		self.url = "https://web.whatsapp.com/"

	def checkOnStatus(self):
		#Make connection to WhatsApp web
		driver = webdriver.Firefox()
		driver.get(self.url)
		time.sleep(15)
		chat_list = driver.find_elements_by_class_name("infinite-list-item")
		for chat in chat_list:
			if chat.find_element_by_class_name("emojitext").text in self.labels:
				chat.click()
				header = driver.find_element_by_id('main')
				body = header.find_element_by_class_name('chat-body')
				time.sleep(5)
				on_stat = False  #Set initial online status to False ,i.e, Not Online
				while True:
					try:
						online = body.find_element_by_class_name('chat-secondary').find_element_by_class_name('emojitext').text
						if online == "online" or online == "typing...":
							if on_stat == False:
								on_stat = True
								on_info = "\n" + self.labels[0] + " : From : " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
								f = open('logs.txt','a')
								f.write(on_info)
								f.close()
					except KeyboardInterrupt:
						break
					except:
						if on_stat == True:
							on_stat = False
							on_info = " Till : " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
							f = open('logs.txt','a')
							f.write(on_info)
							f.close()
						pass

obj = onlineStatus(['Mom'])
obj.checkOnStatus()