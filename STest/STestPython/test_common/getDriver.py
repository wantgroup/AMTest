from selenium import webdriver
import base64
from HTMLReport import AddImage
def driver(browse):
    '''
    获取driver
    url：测试网址
    browse：参数值火狐，谷歌
    '''
    if '谷歌'==browse:
        driver=webdriver.Chrome()
    elif '火狐'==browse:
        driver=webdriver.Firefox()

    return driver

def exit_browse(driver):
    '退出浏览器'
    driver.quit()

def screen_shot(driver,imgName):
    '截屏'
    path=driver.get_screenshot_as_png()
    image = base64.b64encode(path)
    AddImage(image,imgName,imgName)

def assert_case(driver,xpath,assertText):
    str=driver.find_element_by_xpath(xpath).text
    assert assertText == str