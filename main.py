import unittest,time,os
from case.baidu_search_demo import Search
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Search))
    with open('C:\\Users\\CDLX\\.jenkins\\jobs\\webAutomationTestPrj'+'\\TestReport.html','wb') as f:
        HTMLTestRunner(f).run(suite)