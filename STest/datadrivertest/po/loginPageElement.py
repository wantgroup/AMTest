#登录账号输入框
loginNameInput='//*[@id="name"]'
#登录密码输入框
loginPassInput='//*[@id="pass"]'
#登录按钮
loginSubmitButton='//*[@id="signin_form"]/div[3]/input'
def login_name_input():
    return loginNameInput
def login_pass_input():
    return loginPassInput
def login_submit_button():
    return loginSubmitButton




    

if __name__=="__main__":
    print(login_name_input())
