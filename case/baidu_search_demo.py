from selenium import webdriver
import time,unittest,os
from HTMLTestRunner import HTMLTestRunner
# 常用的元素定位方式 第一种 id


class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        global driver
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.dirname(os.path.abspath(__file__))+'/report/'+case_name+'.png'
                self.driver.get_screenshot_as_file(file_path)
        self.driver.quit()

    def start_serach(self,keyword):
        time.sleep(1)
        self.driver.find_element_by_id("kw").send_keys(keyword)
        time.sleep(1)
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        return self.driver.title

    def test_search_huawei(self):
        text = self.start_serach('华为')
        self.assertTrue(text.startswith('华为'))

    def test_search_xiaomi(self):
        text = self.start_serach('小米')
        self.assertTrue(text.startswith('小米'))

    def test_search_vivo(self):
        text = self.start_serach('vivo')
        self.assertTrue(text.startswith('vivo'))

    def test_search_oppo(self):
        text = self.start_serach('oppo')
        self.assertTrue(text.startswith('oppo'))





