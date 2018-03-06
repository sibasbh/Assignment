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
#from ebay_CommonCodes import ebay_CommonCodes
from util.common_methods import BaseClass
from robot.libraries.BuiltIn import BuiltIn
from test_script.suite_1.testsuite import  TestSuite
from robot.utils.asserts import *


html_pass = '<b style="color:green">PASS</b>'
html_fail = '<b style="color:red">FAIL</b>'

class ProduceDetails:
    def __init__(self,commonobj,objSuite):
        self.robot_env = BuiltIn()
        self.commonobj = commonobj
        self.objSuite = objSuite

    def product_detail_page(self):
        """
        :Step 1 : Check if ebay logo is seen in the Product Detail Page.
        :Step 2 : Copy Product Condition , Price , Product Name and seller information to Dictionary.
        :Step 3 : Dictionary created in Step 2 will be used to validate with informations in Shopping cart page.
        :return: Return Dictionary.
        """
        try:
            search_elem = self.commonobj.custom_driver_wait(self.objSuite.ebay_logo)
            assert_not_none(search_elem, "Check if ebay logo is displayed in product detail page")
            self.prod_detail = {}
            key1 = "Condition"
            key2 = "Price"
            key3 = "Produce Name"
            key4 = "Seller Information"
            value_1 = (self.commonobj.custom_element(self.objSuite.cond_value, 'xpath')).text
            assert_not_none(value_1, "Unable to capture Condition")
            price_elem = self.commonobj.custom_element(self.objSuite.price_value, 'xpath')
            value_2 = str(price_elem.text).replace('US ','')
            assert_not_none(value_2, "Unable to capture the Price")
            value_3 = self.commonobj.custom_element(self.objSuite.prod_name, 'xpath').text
            assert_not_none(value_3, "Unable to capture the Product Name")
            value_4 = self.commonobj.custom_element(self.objSuite.seller_information_value, 'xpath').text
            assert_not_none(value_4, "Unable to capture the Product Name")

            self.prod_detail[key1] = value_1
            self.prod_detail[key2] = value_2
            self.prod_detail[key3] = value_3
            self.prod_detail[key4] = value_4

            self.robot_env.log_to_console("Product Detail Page - Captured Product Informations")
            logger.info("\t <b><h3> Product Detail Page - Captured all Product Informations : %s </h3></b>" % html_pass,html=True)
            assert_not_none(self.prod_detail, "Dictionary not created for captured products")
            return self.prod_detail

        except AssertionError as error:
            self.robot_env.log_to_console("Assersion Error: Product Detail Page - Error while Capturing Product Informations" + str(error))
            logger.info("\t <b><h3>Assersion Error: Product Detail Page - Error while Capturing Product Informations : %s </h3></b>" % html_fail, html=True)
            self.commonobj.get_screenshot(self.commonobj.driver, "Product_Detail_Page_Failure")


    def validate_condition_parameter(self):
        """
        Step 1 : From dictionary created from product_detail_page validate if Condition Parameter is Empty.
        Step 2 : Condition parameter should Not be empty
        :return: NONE
        """
        try:
            # import sys, pdb;
            # pdb.Pdb(stdout=sys.__stdout__).set_trace()

            for key, value in self.prod_detail.items():
                if key == 'Condition':
                    assert_not_equal(None,value,"Condition should not be None")
                    assert_not_equal('', value, "Condition should not be None")
                    logger.info("\t <b><h3> Product Detail Page - 'Condition' should not be empty : %s </h3></b>" % html_pass,html=True)
                    self.robot_env.log_to_console("Product Detail Page - 'Condition' should not be empty")
                    break
            cart_elem = self.commonobj.custom_element(self.objSuite.add_cart, 'xpath')
            cart_elem.click()

        except AssertionError as error:
            self.robot_env.log_to_console( "Assersion Error : Product Detail Page - Condition is Empty" + str(error))
            logger.info("\t <b><h3>Assersion Error : Product Detail Page - Condition is Empty : %s </h3></b>" % html_fail,html=True)
            self.commonobj.get_screenshot(self.commonobj.driver, "Product_Detail_Page_Condition_Failure")


    def protection_plan(self):
        """
        Step 1: Handle Protection Plan page if it appears.
        Step 2: Tap on 'No Thanks' button if Protection Plan page appears.
        :return: NONE
        """
        try:
            prot_elem = self.commonobj.custom_element(self.objSuite.prot_plan, 'xpath')
            assert_none(prot_elem,"Continue only if Protection Plan Page is displayed")
            thank_elem = self.commonobj.custom_element(self.objSuite.thank_btn, 'xpath')
            self.commonobj.custom_click(thank_elem, "No Thanks")

        except AssertionError as error:
            self.robot_env.log_to_console( "Assersion Error : Protection Plan - Page Not displayed : " + str(error))
            logger.info("\t <b><h3>Assersion Error : Protection Plan - Page Not displayed : %s </h3></b>" % html_fail,html=True)
