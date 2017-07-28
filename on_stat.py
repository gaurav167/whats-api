from selenium import webdriver
import time

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
				try:
					print('1')
					time.sleep(5)
					online = body.find_element_by_class_name('chat-secondary').find_element_by_class_name('emojitext').text
					print('2')
					if online == "online" or online == "typing...":
						print('Yay! :)')
				except:
					print('Nay :(')


obj = onlineStatus(['Mom'])
obj.checkOnStatus()