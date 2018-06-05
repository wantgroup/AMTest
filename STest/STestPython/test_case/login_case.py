import  unittest2
from test_common    import  getDriver,login
from HTMLReport import logger

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
        login().info('截屏')
        getDriver.screen_shot(self.driver," ")

    def test_login(self):
        '登录'
        login.login_case(self.driver,'testuser3','123456')
