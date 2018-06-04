import  unittest
from alltestcases.login_page import LoginPage
from common.driver_uilts import test_quit
import HTMLReport
from common import fileutils

def suite():
    suite = unittest.TestSuite()
    suite.addTest(LoginPage("test_login"))
    return suite

if __name__ == "__main__":
    reportName=str(str(fileutils.getHour()+fileutils.getMinute())+"测试报告")
    reportPath=str(fileutils.reportPath())
    print(reportName+";"+reportPath)
    runner = HTMLReport.TestRunner(report_file_name=reportName,  # 报告文件名，如果未赋值，将采用“test+时间戳”
                                   output_path=reportPath,  # 保存文件夹名，默认“report”
                                   title='自动化测试报告',  # 报告标题，默认“测试报告”
                                   description='自动化测试Demo',  # 报告描述，默认“测试描述”
                                   thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                                   thread_start_wait=3,  # 各线程启动延迟，默认 0 s
                                   sequential_execution=True,  # 是否按照套件添加(addTests)顺序执行，
                                   # 会等待一个addTests执行完成，再执行下一个，默认 False
                                   # 如果用例中存在 tearDownClass ，建议设置为True，
                                   # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
                                   # lang='en'
                                   lang='cn'  # 支持中文与英文，默认中文
                                   )
    runner.run(suite())


