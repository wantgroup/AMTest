import unittest
from case.test_case1 import CaseTest
from util.server import Server
from util.write_user_command import WriteUserCommand
import multiprocessing
import time

def appium_init():
    #启动appium
	server = Server()
	server.main()

def get_suite(i):
    #创建测试集合
    suite = unittest.TestSuite()
    #添加第一个测试集
    suite.addTest(CaseTest('test_01',i))

    runner = unittest.TextTestRunner()
    runner.run(suite)

def get_count():
    #有几个手机可用
	write_user_file = WriteUserCommand()
	count = write_user_file.get_file_lines()
	return count


if __name__ == '__main__':
    appium_init()
    threads=[]
    for i in  range(0,get_count()):
        t=multiprocessing.Process(target=get_suite,args=[i,])
        threads.append(t)
        time.sleep(3)
    for t in threads:
        t.start()