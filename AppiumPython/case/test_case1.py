#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/cloudin/Desktop/project/AMTest/AppiumPython")

import unittest
import time
from business.login_business import LoginBusiness
from util.write_user_command import WriteUserCommand
from util.tools import Tools
tool = Tools()
rootpath = tool.getRootPath()

class CaseTest(unittest.TestCase):
	def __init__(self, methodName='runTest', param=None):
		super(CaseTest, self).__init__(methodName)
		global parames
		parames = param
		print(parames)

	@classmethod
	def setUpClass(cls):

		print( "setUpclass---->",parames)
		cls.login_business = LoginBusiness(parames)

	def setUp(self):
		print ("this is setup\n")


	def test_01(self):
		self.login_business.login_token()
	
	def tearDown(self):
		#截屏操作
		time.sleep(1)
		print( "this is teardown\n")
		if sys.exc_info()[0]:
			self.login_business.login_handle.login_page.driver.save_screenshot( rootpath+"/jpg/test01.png")


	@classmethod
	def tearDownClass(cls):
		time.sleep(1)
		print ("this is class teardown\n")
		# cls.driver.quit()



