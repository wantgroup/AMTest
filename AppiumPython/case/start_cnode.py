import time
from appium import webdriver

capabilities = {
    "platformName": "Android",
    # "automationName":"UiAutomator2",
    "deviceName": "Y15QKCPH278J4",
    "appPackage":"org.cnodejs.android.md",
    "appActivity": "org.cnodejs.android.md.ui.activity.LaunchActivity",
    "noReset": "true"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
time.sleep(3)
driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.ImageButton").index(0)').click()