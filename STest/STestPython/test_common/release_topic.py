from test_pom   import home_page,release_topic_page
from HTMLReport import logger
from selenium.webdriver.common.action_chains import ActionChains
from test_common    import getDriver

def release_topic(driver,plate,title,content):
    logger().info('点击首页的发布话题')
    driver.find_element_by_xpath(home_page.home_topic_xpath).click()
    driver.find_element_by_xpath(release_topic_page.topic_select_xpath).click()
    if '请选择' == plate:
        driver.find_element_by_xpath(release_topic_page.topic_select_option1_xpath).click()
    elif '分享' == plate:
        logger().info("选择板块分享")
        driver.find_element_by_xpath(release_topic_page.topic_select_option2_xpath).click()
    elif '问答'   == plate:
        logger().info("选择板块问答")
        driver.find_element_by_xpath(release_topic_page.topic_select_option3_xpath).click()
    elif '招聘'   == plate:
        logger().info("选择板块招聘")
        driver.find_element_by_xpath(release_topic_page.topic_select_option4_xpath).click()
    logger().info("填写标题 %s" % title)
    driver.find_element_by_xpath(release_topic_page.topic_title_xpath).send_keys(title)
    logger().info('输入内容 %s' % content)
    el=driver.find_element_by_xpath(release_topic_page.topic_content_xpath)
    ActionChains(driver).click(el).send_keys(content).perform()
    logger().info('点击发布按钮')
    driver.find_element_by_xpath(release_topic_page.topic_submit_xpath).click()
    getDriver.assert_case(driver,release_topic_page.topic_me_release_details_content_xpath,content)
    getDriver.assert_case(driver,release_topic_page.topic_me_release_details_title_xpath,title)
