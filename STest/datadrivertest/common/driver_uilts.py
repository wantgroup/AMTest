from selenium import webdriver


def getDriver(Browser):
    '''
    :param Browser: 谷歌 火狐 IE
    :return: 返回浏览器
    '''
    if Browser == "谷歌":
        driver = webdriver.Chrome()
    elif Browser == "火狐":
        driver = webdriver.Firefox()
    elif Browser == "IE":
        driver = webdriver.Ie()
    return driver

def set_Url(Browser, Url):
    '''
    :param Browser:谷歌 火狐 IE
    :param Url:测试url
    :return:返回打开浏览器的driver
    '''
    driver = getDriver(Browser)
    driver.get(Url)
    return driver
def testlogin(Browser, Url):
    '''
    :param Browser: 谷歌 火狐 IE
    :param Url: 谷歌 火狐 IE
    :return: 返回登录后的driver
    '''
    driver = set_Url(Browser, Url)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/ul/li[6]/a").click()
    driver.find_element_by_xpath('//*[@id="name"]').send_keys('testuser3')
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="signin_form"]/div[3]/input').click()
    return driver
#截屏
def screenShot(driver,filename):
    '''
    :param driver: 要截屏时的driver
    :param filename: 截屏存放的路径
    :return: true   false
    '''
    driver.save_screenshot(filename)
#退出浏览器
def test_quit(driver):
    driver.quit()
#返回截屏数据不保存
def getScreenShotData(driver):
    data=driver.get_screenshot_as_png()
    return data









