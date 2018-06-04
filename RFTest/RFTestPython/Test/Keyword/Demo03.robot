*** Settings ***
Library             SeleniumLibrary
Variables       ../Locators/Demo03.py

***Keywords***
打开网页
    Open Browser  url=${case_url}  browser=chrome  
    Maximize Browser Window
点击登录
    Click Element    link:${login_link_text}
输入登录信息
    Input Text          id:${input_user_id}    ${input_user_text}
    Input Password      id:${input_pwd_id}     ${input_pwd_text}
点击登录按钮
    Click Element          xpath:${login_Buttom_xpath} 
发帖
    Click Element   xpath:${post_message_bottom}
    Click Element   xpath:${select}
    Click Element   xpath:${option}
    Input Text      xpath:${title_xpath}      ${title_text}
    Click Element   xpath://*[@id="create_topic_form"]/fieldset/div/div/div[2]/div[6]
    Execute JavaScript    ${editor_JavaScript}

