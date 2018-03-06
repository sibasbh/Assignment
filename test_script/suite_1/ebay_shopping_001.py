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
from robot.utils.asserts import *


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
                self.robot_env.log_to_console("Landing Page - Browser launched and URL Entered successfully")
                logger.info("\t <b><h3>1.Landing Page - Browser launched and URL Entered successfully : %s </h3></b>" % html_pass, html=True)
                return True
            else:
                return False
        except Exception as e:
            logger.info("\t <b><h3>Exception: FAILED TO LAUNCHED CHROME BROWSER AND ENTER URL : %s </h3></b>" % html_fail, html=True)
            self.robot_env.log_to_console("Exception: FAILED TO LAUNCHED CHROME BROWSER AND ENTER URL", str(e))
            self.chrome.close_driver()


    def test(self):
        """
        Call all the functions created to perform ebay webpage automation.
        :return: NONE
        """
        try:
            flag = self.homeobj.product_search()
            assert_true(flag, "Validate if Search is successful")
            logger.info("\t <b><h3>Landing Page - Product search is successful : %s </h3></b>" % html_pass, html=True)

        except AssertionError as error:
            self.robot_env.log_to_console("Assersion Error : Landing Page - Error during product Search" + str(error))
            logger.info("\t <b><h3>Assersion Error : Landing Page - Error during product Search : %s </h3></b>" % html_fail,html=True)
            self.chrome.get_screenshot(self.chrome.driver, "Product_Search_Failure")


        try:
            flag = self.homeobj.choose_category()
            assert_true(flag, "Validate if choose_category is successful")
            logger.info("\t <b><h3>Landing Page - Identified 50-60 Inch Button : %s </h3></b>" % html_pass, html=True)

        except AssertionError as error:
            self.robot_env.log_to_console("Assersion Error : Landing Page - Unable to identify 50-60 Inch Button" + str(error))
            logger.info("\t <b><h3>Assersion Error : Landing Page - Unable to identify 50-60 Inch Button : %s </h3></b>" % html_fail,html=True)
            self.chrome.get_screenshot(self.chrome.driver, "50-60In_Capture_Failed")


        try:
            flag = self.homeobj.validate_select_product()
            assert_true(flag, "Validate if choose_category is successful")
            logger.info("\t <b><h3> Landing Page - Second product in List contain word 'sony' and 'tv' : %s </h3></b>" % html_pass,html=True)

        except AssertionError as error:
            self.robot_env.log_to_console("Assersion Error : Landing Page - Second Product name does not contain text 'Sony' or 'tv'" + str(error))
            logger.info("\t <b><h3>Assersion Error : Landing Page - Second Product name does not contain text 'Sony' or 'tv' : %s </h3></b>" % html_fail,html=True)
            self.chrome.get_screenshot(self.chrome.driver, "Product_Search_Failure")
            raise Exception("Exception validate select product")



        try:
            self.prod_details = self.prodobj.product_detail_page()
            assert_not_none(self.prod_details, "Dictionary not created for captured products")
            logger.info("\t <b><h3> Product Detail Page - Captured all Product Informations : %s </h3></b>" % html_pass,html=True)

        except AssertionError as error:
            self.robot_env.log_to_console("Assersion Error: Product Detail Page - Error while Capturing Product Informations" + str(error))
            logger.info("\t <b><h3>Assersion Error: Product Detail Page - Error while Capturing Product Informations : %s </h3></b>" % html_fail,html=True)
            self.chrome.get_screenshot(self.chrome.driver, "Product_Detail_Page_Failure")



        try:
            flag=self.prodobj.validate_condition_parameter()
            assert_true(flag, "Validate if condition_parameter is empty")
            logger.info("\t <b><h3> Product Detail Page - 'Condition' should not be empty : %s </h3></b>" % html_pass,html=True)
        except AssertionError as error:
            self.robot_env.log_to_console("Assersion Error : Product Detail Page - Condition is Empty" + str(error))
            logger.info("\t <b><h3>Assersion Error : Product Detail Page - Condition is Empty : %s </h3></b>" % html_fail,html=True)
            self.chrome.get_screenshot(self.chrome.driver, "Product_Detail_Page_Condition_Failure")


        try:
            flag=self.prodobj.protection_plan()
            assert_true(flag, "Validate if protection plan is displayed")
            logger.info("\t <b><h3> Protection Plan - Page Not displayed and handled : %s </h3></b>" % html_pass,html=True)
        except AssertionError as error:
            self.robot_env.log_to_console("Assersion Error : Protection Plan - Page Not displayed : " + str(error))
            logger.info("\t <b><h3>Assersion Error : Protection Plan - Page Not displayed : %s </h3></b>" % html_pass,html=True)


        try:
            self.prod_details_Cart = self.cartobj.shoppingcart_page_validation()
            assert_not_none(self.prod_details_Cart, "Dictionary not created for captured products")
            logger.info("\t <b><h3> Shopping Cart Page - Captured all Product Informations : %s </h3></b>" % html_pass, html=True)
        except AssertionError as error:
            self.robot_env.log_to_console("Assersion Error : Shopping Cart - Error occured during product detail capture" + str(error))
            logger.info("\t <b><h3>Assersion Error : Shopping Cart - Error occured during product detail capture : %s </h3></b>" % html_fail,html=True)
            self.chrome.get_screenshot(self.chrome.driver, "ShoppingCart_Failure")


        try:
            flag_value = self.cartobj.product_detail_validation(self.prod_details)
            assert flag_value == 4 ,"Product details mismatch in Shopping cart and prod details pages"
            logger.info("\t <b><h3>Shopping Cart - All Parameters from Product Details page and Shopping Cart Page should match : %s </h2></b>" % html_pass,html=True)

        except AssertionError as error:
            self.robot_env.log_to_console("Assersion Error : Parameters from Product Detail page does not match Shopping Cart Page" + str(error))
            logger.info("\t <b><h3>Assersion Error : Error occured during product detail capture from Shopping Cart : %s </h3></b>" % html_fail,html=True)
            self.chrome.get_screenshot(self.chrome.driver, "ShoppingCart_Validation_Failure")
            raise Exception("Exception product detail validation")

    def cleanup(self):
        """
        Close the chrome browser gracefully
        :return: NONE
        """
        self.chrome.close_driver()
