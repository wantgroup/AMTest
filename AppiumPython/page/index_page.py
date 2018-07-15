#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from util.get_by_local import GetByLocal
import time
from base.base_driver import BaseDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IndexPage:

    def __init__(self,i):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)
	
    # 首页侧边栏按钮
    def get_traggle_button(self):
        return self.get_by_local.get_element('traggle_button')
    
    # 头像
    def get_avatar_button(self):
        return self.get_by_local.get_element('avatar')
    
