import  unittest2
from test_common    import  getDriver,login
from HTMLReport import logger
from test_utils import utilsApi

class   LoginCase(unittest2.TestCase):
    '登录和注册'
    url='http://118.31.19.120:3000/'
    browse='谷歌'
    logger().info('打开浏览器获取driver')
    driver=getDriver.driver(url,browse)

    @classmethod
    def tearDownClass(self):
        logger().info('退出浏览器')
        getDriver.exit_browse(self.driver)

    def tearDown(self):
        logger().info("截屏")
        print(utilsApi.get_function_name())
        getDriver.screen_shot(self.driver,utilsApi.get_function_name())

    def test_login(self):
        '登录'
        login.login_case(self.driver,'testuser3','123456')
