from selenium import webdriver

def driver(url,browse):
    '''
    获取driver
    url：测试网址
    browse：参数值火狐，谷歌
    '''
    if '谷歌'==browse:
        driver=webdriver.Chrome()
    elif '火狐'==browse:
        driver=webdriver.Firefox()
    return driver.get(url)

def exit_browse(driver):
    '退出浏览器'
    driver.quit()