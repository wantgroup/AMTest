***Settings***
Library     SeleniumLibrary
Variables       ./test02values.py

***Test Cases***
测试登录
    [Setup]
        打开页面
        Maximize Browser Window
    输入登录信息
    [Teardown]
        Close Browser

***Keywords***
打开页面
    Open Browser    ${url}      chrome
    Click Element   xpath:${loninbuttom_xpath}

输入登录信息
    Input Text      xpath:${userName_xpath}   ${userName}
    Input Password  xpath:${password_xpath}   ${password}
    Capture Page Screenshot     filename=test02.png
