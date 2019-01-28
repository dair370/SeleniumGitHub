import unittest
from selenium import webdriver
import time

class EasySign(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://autofms.devtest.tk/index/login?next=%2F')

    def test_singin(self):
        driver = self.driver
        print(driver.current_url)
        print(driver.title)
        self.assertEqual(driver.title, "登入 | autofms 導覽列", "網站標題不正確")
        time.sleep(1)
        driver.find_element_by_name('account').send_keys('admin')
        driver.find_element_by_name('password').send_keys('111111')
        driver.find_element_by_class_name("btn-primary").click()
        time.sleep(2)
        Banner = driver.find_element_by_xpath('//*[@id="page-banner"]').text
        print(Banner)
        self.assertEqual(Banner, "autofms Banner", "Banner不正確")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)