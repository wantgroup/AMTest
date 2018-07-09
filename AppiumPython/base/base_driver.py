# coding=utf-8
import os
import time
from appium import webdriver
from util.write_user_command import WriteUserCommand
from util.tools import Tools


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
        time.sleep(10)
        return driver

if __name__=="__main__":
    d=BaseDriver().android_driver()