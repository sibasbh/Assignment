import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from datetime import datetime
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from util.common_methods import BaseClass
from test_script.suite_1.testsuite import TestSuite
from POM.home_page import HomePage
from POM.product_detail_page import ProduceDetails
from POM.check_out_page import ShoppingCart


html_pass = '<b style="color:green">PASS</b>'
html_fail = '<b style="color:red">FAIL</b>'

class ebay_shopping_001(object):
    def __init__(self):
        pass
    def testcase001_initialize(self, testname):
        """
        :Step 1 : Function called from Suite_1.text file with Argument PRODUCT_VALIDATION
        :Step 2 : Call Class PRODUCT_VALIDATION with 001 as the testcases ID
        :param testname: Argument PRODUCT_VALIDATION passed from suit_1.text file
        :return: NONE
        """
        robot_env = BuiltIn()
        robot_env.log_to_console("****EXECUTION STARTS HERE****")
        self.tc = globals()[testname]
        self.tc = self.tc("001")
        self.tc.initialize()
    def testcase_setup(self):
        """
        Call Setup method to initialise Chrome Driver.
        :return: NONE
        """
        self.tc.setup()
    def testcase_test(self):
        """
        Call test method to start the Script execution.
        :return: NONE
        """
        self.tc.test()
    def testcase_cleanup(self):
        """
        Close chrome driver
        :return: NONE
        """
        self.tc.cleanup()


class PRODUCT_VALIDATION():
    def __init__(self, testid):
        self.testid = testid

    def initialize(self):
        """
        Create object for Class Testsuite which is under testsuite.py
        :return: NONE
        """
        self.objSuite = TestSuite(self.testid)

    def setup(self):
        """
        :Step 1 : Set Testcase number to 001
        :Step 2 : Initialise Chrome Driver , Maximise the Screen and create objects for all the python files (Pages).
        :return: NONE
        """
        try:
            if self.testid == "001":
                self.robot_env = BuiltIn()
                self.chrome = BaseClass('chrome')
                self.homeobj = HomePage(self.chrome, self.objSuite)
                self.prodobj = ProduceDetails(self.chrome, self.objSuite)
                self.cartobj = ShoppingCart(self.chrome, self.objSuite)
                self.chrome.driver.maximize_window()
                self.chrome.driver.get(self.objSuite.url)
                self.robot_env.log_to_console("1. CHROME BROWSER LAUNCHED AND URL ENTERED")
                logger.info("\t <b><h3>CHROME BROWSER LAUNCHED AND URL ENTERED : %s </h3></b>" % html_pass, html=True)
                self.chrome.get_screenshot(self.chrome.driver, "1_Landing Page_Success")
        except Exception as e:
            logger.info("\t <b><h3>FAILED TO LAUNCHED CHROME BROWSER AND ENTER URL : %s </h3></b>" % html_fail, html=True)
            self.chrome.driver.close_driver()


    def test(self):
        """
        Call all the functions created to perform ebay webpage automation.
        :return: NONE
        """
        self.homeobj.product_search()
        self.homeobj.choose_category()
        self.homeobj.validate_select_product()
        self.prod_details = self.prodobj.product_detail_page()
        self.prodobj.validate_condition_parameter()
        self.prodobj.protection_plan()
        self.cartobj.shoppingcart_page_validation()
        self.cartobj.product_detail_validation(self.prod_details)

    def cleanup(self):
        """
        Close the chrome browser gracefully
        :return: NONE
        """
        self.chrome.close_driver()
