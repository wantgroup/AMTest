# coding=utf-8
import os
from util.get_by_local import  GetByLocal
from appium import webdriver
from util.write_user_command import WriteUserCommand
from util.tools import Tools
import time

class BaseDriver:

    def android_driver(self, i):
        tool = Tools()
        rootpath = tool.getRootPath()
        apkpath = os.path.join(rootpath, 'apks', 'cnode.apk')
        print("this is android_driver:", i)
        # devices_name adb devices
        # port
        write_file = WriteUserCommand()
        devices = write_file.get_value('user_info_' + str(i), 'deviceName')
        port = write_file.get_value('user_info_' + str(i), 'port')
        capabilities = {
            "platformName": "Android",
            "deviceName": devices,
            "app": apkpath,
            "appWaitActivity": "org.cnodejs.android.md.ui.activity.LaunchActivity",
            "noReset": "true",
            # "platforVersion": "5.1",
            "appPackage": "org.cnodejs.android.md"
        }
        driver = webdriver.Remote(
            "http://127.0.0.1:" + port + "/wd/hub", capabilities)

        return driver
def test_1():
    tool = Tools()
    rootpath = tool.getRootPath()
    apkpath = os.path.join(rootpath, 'apks', 'cnode.apk')
    write_file = WriteUserCommand()
    capabilities = {
        "platformName": "Android",
        "deviceName": "36165441",
        "app": apkpath,
        "appWaitActivity": "org.cnodejs.android.md.ui.activity.LaunchActivity",
        "noReset": "true",
        "appPackage": "org.cnodejs.android.md",
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }
    driver = webdriver.Remote("http://127.0.0.1:" + str(4723) + "/wd/hub", capabilities)
    # driver.get_window_size()["height"]
    # width=driver.get_window_size()["width"]
    time.sleep(5)
    driver.find_element_by_android_uiautomator(
        'new UiSelector().className("android.widget.ImageButton")').click()
    driver.find_element_by_id("org.cnodejs.android.md:id/tv_login_name").click()
    time.sleep(5)
    driver.find_element_by_id("org.cnodejs.android.md:id/edt_access_token").send_keys("fgdgdfsgsdf")
    driver.find_element_by_id("org.cnodejs.android.md:id/btn_login").click()
    # em=GetByLocal(driver)
    # s1=em.get_element("traggle_button")
    # print(s1)
    # s1.click()
    # s2=em.get_element("avatar")
    # s2.click()
    # s3=em.get_element("token")
    # s3.send_keys("safsgdfsg")
    # s4=em.get_element("login_button")
    # s4.click()

if __name__=="__main__":
    test_1()
