import unittest
from selenium import webdriver
import time
import HTMLTestRunnerCN

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.bro = webdriver.Chrome()
        self.bro.maximize_window()
        self.bro.get('http://rwd.devtest.tk')

    def test_login(self):
        acc = 'user5'
        pwd = '111111'
        self.bro.find_element_by_link_text('登入').click()
        time.sleep(1)

        self.bro.find_element_by_name('account').send_keys(acc)
        time.sleep(1)
        self.bro.find_element_by_name('password').send_keys(pwd)
        time.sleep(1)
        self.bro.find_element_by_xpath('//*[@id="login_form"]/div[5]/div/button').click()
        time.sleep(1)

        head = self.bro.find_element_by_xpath('//*[@id="page-sysbar"]/nav/div/div[3]/ul/li[6]/a')
        print(head.text)


    def tearDown(self):
        print('測試結束')
        time.sleep(1)
        self.bro.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginTest('test_login'))
    #确定生成报告的路径
    filePath ='C:\\Users\\User\\Desktop\\CI\\report.html'
    fp = open(filePath,'wb')
    #生成报告的Title,描述
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title='{ Test Report }',
        #description='详细测试用例结果',
        tester='Chen'
        )
    #运行测试用例
    runner.run(suite)
    #runner.run(Suite())
    # 关闭文件，否则会无法生成文件
    fp.close()