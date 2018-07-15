#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from util.get_by_local import GetByLocal
import time
from base.base_driver import BaseDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
	# 获取登录页面所有的页面元素信息
	def __init__(self,i):
		base_driver = BaseDriver()
		self.driver = base_driver.android_driver(i)
		self.get_by_local = GetByLocal(self.driver)

	

	def get_token_element(self):
		'''
		获取token元素信息
		'''
		return self.get_by_local.get_element('token')


	def get_login_button_element(self):
		'''
		获取登陆按钮元素信息
		'''
		return self.get_by_local.get_element('login_button')

	def get_GitHub_element(self):
		'''
		GitHub登录元素
		'''
		return self.get_by_local.get_element('github_button')

	def get_qcode_element(self):
		'''
		二维码扫面登录元素
		'''
		return self.get_by_local.get_element('qr_code_button')