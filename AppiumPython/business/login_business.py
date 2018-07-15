#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import time
from handle.login_handle import LoginHandle

#操作
class LoginBusiness(object):
    def __init__(self, driver):
        self.login_handle = LoginHandle(driver)

    def login_token(self):
        '''
        登录
        :return:
        '''
        time.sleep(5)
        self.login_handle.click_traggle_button()
        self.login_handle.click_avatar_button()
        time.sleep(5)
        # self.login_handle.send_token_val("xxxxxxxxxxx")
        self.login_handle.send_token_val()
        self.login_handle.click_login()
