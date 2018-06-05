import  unittest2
from test_common    import  getDriver,login

class   LoginCase(unittest2.TestCase):
    url='http://118.31.19.120:3000/'
    browse='谷歌'
    driver=getDriver.driver(url,browse)
    def tearDownClass(self):
        getDriver.exit_browse(self.driver)
    def test_login(self):
        '登录'
        login.login_case(self.driver,'testuser3','123456')
