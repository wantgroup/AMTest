# coding=utf-8
from handle.login_handle import LoginHandle


class LoginBusiness(object):
    def __init__(self, i):
        self.login_handle = LoginHandle(i)

    def login_token(self):
        self.login_handle.click_traggle_button()
        self.login_handle.click_avatar_button()
        self.login_handle.send_token_val("xxxxxxxxxxx")
        self.login_handle.click_login()
