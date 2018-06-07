from test_pom   import  home_page,login_page
from HTMLReport import logger

def login_case(driver,url,userName,password):
    driver.get(url)
    logger().info('点击首页的登录按钮')
    driver.find_element_by_link_text(home_page.home_login_link_text).click()
    logger().info('输入登录用户名 %s' % userName)
    driver.find_element_by_id(login_page.login_userName_id).send_keys(userName)
    logger().info('输入登录密码 %s' % password)
    driver.find_element_by_id(login_page.login_password_id).send_keys(password)
    logger().info('点击登录按钮')
    driver.find_element_by_css_selector(login_page.login_submit_css_selector).click()
    return driver

