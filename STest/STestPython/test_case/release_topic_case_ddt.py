import  unittest2
from test_common    import  getDriver,login
from HTMLReport import logger
from test_utils import utilsApi
from test_pom import home_page,release_topic_page
from selenium.webdriver.common.action_chains import ActionChains

class   ReleasdTopic(unittest2.TestCase):
    '登录'
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

    def tearDown(self):
        logger().info("截屏")
        getDriver.screen_shot(self.driver,self.imgName)

    def test_topic(self,):
        '登录'
        self.imgName=utilsApi.get_function_name()
        login.login_case(self.driver,self.url,'testuser3','123456')
        logger().info('点击首页的发布话题')
        self.driver.find_element_by_xpath(home_page.home_topic_xpath).click()
        self.driver.find_element_by_xpath(release_topic_page.topic_select_xpath).click()
        if '请选择' == plate:
            self.driver.find_element_by_xpath(release_topic_page.topic_select_option1_xpath).click()
        elif '分享' == plate:
            logger().info("选择板块分享")
            self.driver.find_element_by_xpath(release_topic_page.topic_select_option2_xpath).click()
        elif '问答' == plate:
            logger().info("选择板块问答")
            self.driver.find_element_by_xpath(release_topic_page.topic_select_option3_xpath).click()
        elif '招聘' == plate:
            logger().info("选择板块招聘")
            self.driver.find_element_by_xpath(release_topic_page.topic_select_option4_xpath).click()
        logger().info("填写标题 %s" % title)
        self.driver.find_element_by_xpath(release_topic_page.topic_title_xpath).send_keys(title)
        logger().info('输入内容 %s' % content)
        el = self.driver.find_element_by_xpath(release_topic_page.topic_content_xpath)
        ActionChains(self.driver).click(el).send_keys(content).perform()
        logger().info('点击发布按钮')
        self.driver.find_element_by_xpath(release_topic_page.topic_submit_xpath).click()
        getDriver.assert_case(self.driver, release_topic_page.topic_me_release_details_content_xpath, content)
        getDriver.assert_case(self.driver, release_topic_page.topic_me_release_details_title_xpath, title)

if __name__=='__main__':
    unittest2.main()

