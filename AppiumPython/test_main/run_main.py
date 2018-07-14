from case.test_case1 import CaseTest
import unittest
from util.server import Server
from util.write_user_command import WriteUserCommand
import multiprocessing
import time
import HTMLReport
from util import  utilsApi

def appium_init():
    #启动appium
	server = Server()
	server.main()

def get_suite(i):
    #创建测试集合
    suite = unittest.TestSuite()
    #添加第一个测试集
    suite.addTest(CaseTest('test_01',i))

    reportPath=utilsApi.reportPath()

    runner = HTMLReport.TestRunner(report_file_name="论坛测试报告"+str(i),  # 报告文件名，如果未赋值，将采用“test+时间戳”
                                   output_path=reportPath,  # 保存文件夹名，默认“report”
                                   title='测试报告',  # 报告标题，默认“测试报告”
                                   description='测试报告',  # 报告描述，默认“测试描述”
                                   thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                                   thread_start_wait=3,  # 各线程启动延迟，默认 0 s
                                   sequential_execution=True,  # 是否按照套件添加(addTests)顺序执行，
                                   # 会等待一个addTests执行完成，再执行下一个，默认 False
                                   # 如果用例中存在 tearDownClass ，建议设置为True，
                                   # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
                                   # lang='en'
                                   lang='cn'  # 支持中文与英文，默认中文
                                   )
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