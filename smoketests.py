import unittest
from fastname import OpenTest
from easysignin import EasySign
# get all tests from SearchProductTest and HomePageTest class
fastname = unittest.TestLoader().loadTestsFromTestCase(OpenTest)
easysignin  = unittest.TestLoader().loadTestsFromTestCase(EasySign)
# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([fastname, easysignin])
# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)