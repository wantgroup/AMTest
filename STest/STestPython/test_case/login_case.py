import  unittest2
from test_common    import  getDriver,login
from HTMLReport import logger
from test_utils import utilsApi
from ddt    import ddt,unpack,data

@ddt
class   LoginCase(unittest2.TestCase):
    '登录和注册'
    url='http://118.31.19.120:3000/'
    browse='谷歌'
    logger().info('打开浏览器获取driver')
    driver=getDriver.driver(browse)
    imgName=None
    @classmethod
    def tearDownClass(self):
        logger().info('退出浏览器')
        getDriver.exit_browse(self.driver)

    def setUp(self):
        self.imgName=None
        self.driver.delete_all_cookies()

    def tearDown(self):
        logger().info("截屏")
        getDriver.screen_shot(self.driver,self.imgName)

    @data(["testuser3","123456"],["testuser4","123456"])
    def test_login(self,values):
        '登录'
        self.imgName=utilsApi.get_function_name()
        login.login_case(self.driver,self.url,values[0],values[1])

# if __name__=='__main__':
#     unittest2.main()