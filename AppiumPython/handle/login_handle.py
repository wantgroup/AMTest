#coding=utf-8

from page.login_page import LoginPage
from page.index_page import IndexPage

class LoginHandle:
	def __init__(self,i):
		self.login_page = LoginPage(i)
		self.index_page = IndexPage(i)
	
	#操作登录页面的元素
	def click_traggle_button(self):
		self.index_page.get_traggle_button().click()
	
	def click_avatar_button(self):
		"""
		点击头像
		"""
		self.index_page.get_avatar_button().click()


	def click_login(self):
		"""
		点击登录按钮
		"""
		self.login_page.get_login_button_element().click()
	
	def send_token_val(self,token):
		"""
		输入token
		"""
		self.login_page.get_token_element().send_keys(token)
