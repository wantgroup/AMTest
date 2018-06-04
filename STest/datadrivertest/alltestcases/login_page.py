import unittest
from HTMLReport import logger,AddImage
from common import driver_uilts,fileutils
import time
from po import loginPageElement as loginpage
import base64

class LoginPage(unittest.TestCase):
    "登录页面相关的操作"

    # 获取打开浏览器后的driver
    driver=driver_uilts.set_Url('谷歌',"http://118.31.19.120:3000/")

    @classmethod
    def tearDownClass(cls):
        "退出浏览器"
        driver_uilts.test_quit(cls.driver)

    def tearDown(self):
        '截屏'
        fileutils.addReportImg(self.driver)
    def test_login(self):
        "登录"
        logger().info('点击首页登录按钮')
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/ul/li[6]/a").click()
        logger().info('输入账号：testuser3')
        self.driver.find_element_by_xpath(loginpage.login_name_input()).send_keys('testuser3')
        logger().info('输入密码：123456')
        self.driver.find_element_by_xpath(loginpage.login_pass_input()).send_keys('123456')
        logger().info('点击登录按钮')
        self.driver.find_element_by_xpath(loginpage.login_submit_button()).click()



