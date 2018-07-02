#!/usr/bin/python
#coding=utf-8
import  unittest2
from test_common    import  getDriver,login
from HTMLReport import logger
from test_utils import utilsApi
from ddt    import ddt,unpack,data
from test_pom   import home_page,login_page

@ddt
class   LoginCase(unittest2.TestCase):
    '登录'
    url=None
    driver=None
    imgName=None

    @classmethod
    def setUpClass(cls):
        global url,browse,driver
        cls.url= 'http://118.31.19.120:3000/'
        cls.driver = getDriver.driver('谷歌')

    @classmethod
    def tearDownClass(self):
        logger().info('退出浏览器')
        getDriver.exit_browse(self.driver)

    def setUp(self):
        self.imgName=None


    def tearDown(self):
        logger().info("截屏")
        getDriver.screen_shot(self.driver,self.imgName)
        self.driver.delete_all_cookies()

    @data(*utilsApi.get_data_csv(utilsApi.superiorPath()+'/test_data/loginData.csv'))
    @unpack
    def test_login(self,values1,values2,values3,values4):
        '登录'
        self.imgName=utilsApi.get_function_name()
        login.login_case(self.driver,self.url,values1,values2)
        if  'success'  == values3:
            getDriver.assert_case(self.driver,home_page.home_userName_xpath,values4)
        else:
            getDriver.assert_case(self.driver,login_page.login_errortext_xpath, values4)

if __name__=='__main__':
    unittest2.main()