from selenium import webdriver
import unittest
import time
import HTMLTestRunner

class OpenTest(unittest.TestCase):
    # 初始化測試環境
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://autofms.devtest.tk/')

    # 測試主體
    def testCase(self):
        self.driver.maximize_window()

    # 收尾工作
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test = unittest.TestSuite()
    test.addTest(OpenTest('testCase'))
    file_result = open('C:\\Users\\User\\Desktop\\CI\\report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title=u'測試報告', description=u'用例執行情況')
    runner.run(test)
    file_result.close()