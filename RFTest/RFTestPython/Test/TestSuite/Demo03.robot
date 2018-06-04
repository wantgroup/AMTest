*** Settings ***
Library     SeleniumLibrary
Variables       ../Locators/Demo03.py
Resource        ../Keyword/Demo03.robot

*** Test Cases ***
测试登录
    [Setup]
        打开网页
    点击登录
    输入登录信息
    点击登录按钮
    发帖
    # [Teardown]
    #     Close Browser
    