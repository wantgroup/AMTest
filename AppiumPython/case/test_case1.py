#coding=utf-8
import sys
sys.path.append("D:\python学习\AppiumPython")

import unittest
import multiprocessing
from util.server import Server
import time
from business.login_business import LoginBusiness
from util.write_user_command import WriteUserCommand
from util.tools import Tools
tool = Tools()
rootpath = tool.getRootPath()

class ParameTestCase(unittest.TestCase):

	def __init__(self,methodName='runTest',parame=None):
		super(ParameTestCase,self).__init__(methodName)
		global parames
		parames = parame

class CaseTest(ParameTestCase):

	@classmethod
	def setUpClass(cls):
		print( "setUpclass---->",parames)
		cls.login_business = LoginBusiness(parames)

	def setUp(self):
		print ("this is setup\n")


	def test_01(self):
		self.login_business.login_token()
	
	def tearDown(self):
		time.sleep(1)
		print( "this is teardown\n")
		if sys.exc_info()[0]:
			self.login_business.login_handle.login_page.driver.save_screenshot( rootpath+"/jpg/test01.png")


	@classmethod
	def tearDownClass(cls):
		time.sleep(1)
		print ("this is class teardown\n")
		# cls.driver.quit()

def appium_init():
	server = Server()
	server.main()


def get_count():
	write_user_file = WriteUserCommand()
	count = write_user_file.get_file_lines()
	return count

def get_suite(i):
    suite = unittest.TestSuite()
    suite.addTest(CaseTest('test_01',parame=i))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
	appium_init()

	# threads = []
	# for i in range(get_count()):
	# 	print( i)
	# 	t = multiprocessing.Process(target=get_suite,args=(i,))
	# 	threads.append(t)
	# for j in threads:
	# 	j.start()
    #
	# 	time.sleep(1)
	# time.sleep(80)
