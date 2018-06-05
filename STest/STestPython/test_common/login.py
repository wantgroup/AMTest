from test_pom   import  home_page,login_page
def login_case(driver,userName,password):
    driver.find_element_by_link_text(home_page.home_login_link_text).click()
    driver.find_element_by_id(login_page.login_userName_id).send_keys(userName)
    driver.find_element_by_id(login_page.login_password_id).send_keys(password)
    driver.find_element_by_css_selector(login_page.login_submit_css_selector).click()
