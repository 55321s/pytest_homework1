import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml

class TestWework:
	#复用浏览器
	def test_get_cookie(self):
		opt = webdriver.ChromeOptions()
		#设置debug地址
		opt.debugger_address= '127.0.0.1:9222'
		driver = webdriver.Chrome(options=opt)
		driver.implicitly_wait(10)
		driver.get('https://work.weixin.qq.com/wework_admin/frame')
		#driver.find_element(By.ID,'menu_contacts').click()
		#print(driver.get_cookies())
		#获取cookie,序列化后存入yaml文件内
		cookies= driver.get_cookies()
		#for cookie in cookies:
		#	driver.add_cookie(cookie)
		with open('datacookie.yml','w',encoding='UTF-8') as f:
			yaml.dump(cookies,f)
		print(cookies)

	def test_login(self):
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.implicitly_wait(10)
		#登录页面
		driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
		with open('datacookie.yml',encoding='UTF-8') as f:
			yaml_data=yaml.safe_load(f)
			for cookie in yaml_data:
				driver.add_cookie(cookie)
		driver.get('https://work.weixin.qq.com/wework_admin/frame')
		driver.find_element(By.ID, 'menu_contacts').click()
		time.sleep(2)
		driver.find_element(By.XPATH,'//div[@class="ww_operationBar"]/a[1]').click()
		time.sleep(2)

		driver.find_element(By.ID,'username').send_keys('张三')
		driver.find_element(By.ID,'memberAdd_acctid').send_keys('1234')
		driver.find_element(By.ID,'memberAdd_phone').send_keys('15112341236')
		time.sleep(2)
		driver.find_element(By.LINK_TEXT,"保存").click()
		time.sleep(2)
		names=driver.find_elements(By.XPATH,'//tbody[@id="member_list"]/tr/td[2]/span')
		list = []
		for name in names:
			list.append(name.text)
		#print(list)
		assert '张三' in list



