from ddt import ddt, data, file_data, unpack
from selenium import webdriver
import unittest
import time

@ddt
class testddt(unittest.TestCase):
    driver = webdriver.Chrome()
    @data(['testuser3','123456'],[' ','123456'])
    def test_login(self,values1):
        time.sleep(3)
        self.driver.delete_all_cookies()
        self.driver.get('http://118.31.19.120:3000')
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/ul/li[6]/a").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(values1[0])
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(values1[1])
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="signin_form"]/div[3]/input').click()


if __name__=="__main__":
    unittest.main()