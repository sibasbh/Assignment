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
from test_script.suite_1.testsuite import  TestSuite
from robot.utils.asserts import *

html_pass = '<b style="color:green">PASS</b>'
html_fail = '<b style="color:red">FAIL</b>'

class HomePage:
    def __init__(self,commonobj,objSuite):
        self.robot_env = BuiltIn()
        self.commonobj = commonobj
        self.objSuite = objSuite

    def product_search(self):
        """
        :Step 1 : Identify if Search Bar is Clickable.
        :Step 2: Once Step1 is satisfied enter Product name in search bar.
        :Step 3: Click on search.
        :return: NONE
        """
        try:
            search_elem = self.commonobj.custom_driver_wait(self.objSuite.search_br)
            self.commonobj.custom_click(search_elem,"SEARCH BAR")
            self.robot_env.log_to_console('SEARCH BAR LOCATED SUCCESSFULLY')
            elem = self.commonobj.custom_element(self.objSuite.search_br , 'xpath')
            flag = self.commonobj.custom_send_key(elem , self.objSuite.input_item)
            assert_true(flag, "Validate if Search is successful")
            elem.send_keys(Keys.RETURN)
            self.robot_env.log_to_console('Product search is successful')
            logger.info("\t <b><h3>Landing Page - Product search is successful : %s </h3></b>" % html_pass, html=True)

        except AssertionError as error:
            self.robot_env.log_to_console("Assersion Error : Landing Page - Error during product Search" + str(error))
            logger.info("\t <b><h3>Assersion Error : Landing Page - Error during product Search : %s </h3></b>" % html_fail, html=True)
            self.commonobj.get_screenshot(self.commonobj.driver, "Product_Search_Failure")



    def choose_category(self):
        """
        :Step 1: Identify Button 50"-60" and click.
        :Step 2: If Button 50" - 60" is not visible select Next Button and look for the button and click.
        :return: NONE
        """
        try:
            flag = 0
            button_elem = self.commonobj.custom_element(self.objSuite.inch_search , "xpath")
            while (flag == 0):
                if button_elem.is_displayed():
                    self.commonobj.custom_click(button_elem, "INCH BUTTON SELECTION")
                    flag = 1
                else:
                    elem = self.commonobj.custom_element(self.objSuite.search_br , "xpath")
                    self.commonobj.custom_click(elem, "NEXT BUTTON")

            assert flag==1 , "Identified 50-60 Inch Button"
            logger.info("\t <b><h3>Landing Page - Identified 50-60 Inch Button : %s </h3></b>" % html_pass,html=True)

        except AssertionError as error:
            self.robot_env.log_to_console("Assersion Error : Landing Page - Unable to identify 50-60 Inch Button" + str(error))
            logger.info("\t <b><h3>Assersion Error : Landing Page - Unable to identify 50-60 Inch Button : %s </h3></b>" % html_fail, html=True)
            self.commonobj.get_screenshot(self.commonobj.driver, "50-60In_Capture_Failed")



    def validate_select_product(self):
        """
        :Step 1 : Check if the First Product in the List has key word "Sony" and "Tv" .
        :Step 2 : If the Item satisfies Condition 1 Click to Image of the Item.
        :return:
        """
        try:
            result_elem = self.commonobj.custom_driver_wait(self.objSuite.result_kw)
            if result_elem:
                itemlist = self.commonobj.custom_element(self.objSuite.itemtitle , element_name="multi_css")
                assert 'sony' in itemlist[1].text.lower()
                assert 'tv' in itemlist[1].text.lower()
                if 'sony' and 'tv' in itemlist[1].text.lower():
                    self.robot_env.log_to_console("Landing Page - Second product in List contain word 'sony' and 'tv'")
                    logger.info("\t <b><h3> Landing Page - Second product in List contain word 'sony' and 'tv' : %s </h3></b>" % html_pass, html=True)
                    prod_image = self.commonobj.custom_element(self.objSuite.itemimg, element_name="multi_css")
                    prod_image[1].click()

        except AssertionError as error:
            self.robot_env.log_to_console("Assersion Error : Landing Page - Second Product name does not contain text 'Sony' or 'tv'" + str(error))
            logger.info("\t <b><h3>Assersion Error : Landing Page - Second Product name does not contain text 'Sony' or 'tv' : %s </h3></b>" % html_fail, html=True)
            self.commonobj.get_screenshot(self.commonobj.driver, "Product_Search_Failure")
