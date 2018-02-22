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
            self.robot_env.log_to_console('2. SEARCH BAR LOCATED SUCCESSFULLY')
            elem = self.commonobj.custom_element(self.objSuite.search_br , 'xpath')
            self.commonobj.custom_send_key(elem , self.objSuite.input_item)
            elem.send_keys(Keys.RETURN)
            self.robot_env.log_to_console('3. PRODUCT SEARCH SUCCESSFULLY')
            logger.info("\t <b><h3>PRODUCT SEARCH SUCCESSFULLY : %s </h3></b>" % html_pass, html=True)
            self.commonobj.get_screenshot(self.commonobj.driver, "2_Product Searched_Success")

        except Exception as e:
            self.robot_env.log_to_console("FAILED DURING CATEGORY SELECTION :" + str(e))
            logger.info("\t <b><h3>FAILED DURING CATEGORY SELECTION : %s </h3></b>" % html_fail, html=True)
            self.commonobj.get_screenshot(self.commonobj.driver, "2_Product Search_failed")
            self.commonobj.close_driver()



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
                    self.robot_env.log_to_console('4. IDENTIFIED 50-60" BUTTON')
                    logger.info("\t <b><h3> IDENTIFIED 50-60 BUTTON : %s </h3></b>" % html_pass, html=True)
                    flag = 1
                else:
                    elem = self.commonobj.custom_element(self.objSuite.search_br , "xpath")
                    self.commonobj.custom_click(elem, "NEXT BUTTON")
            self.commonobj.get_screenshot(self.commonobj.driver, "3_InchSelection_Success")

        except Exception as e:
            self.robot_env.log_to_console("FAILED DURING CATEGORY SELECTION :" + str(e))
            logger.info("\t <b><h3> FAILED TO IDENTIFY 50-60 BUTTON : %s </h3></b>" % html_fail, html=True)
            self.commonobj.get_screenshot(self.commonobj.driver, "3_InchSelection_Failed")
            self.commonobj.close_driver()




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
                if 'sony' in itemlist[0].text.lower():
                    if 'tv' in itemlist[0].text.lower():
                        self.robot_env.log_to_console("5. PRODUCT WITH 'SONY' 'TV' LOCATED SUCCESSFULLY")
                        logger.info("\t <b><h3> PRODUCT WITH 'SONY' 'TV' LOCATED SUCCESSFULLY: %s </h3></b>" % html_pass, html=True)
                        prod_image = self.commonobj.custom_element(self.objSuite.itemimg, element_name="multi_css")
                        prod_image[0].click()
                else:
                    logger.info("\t <b><h3> FAILED TO IDENTIFY PRODUCT WITH 'SONY' 'TV' : %s </h3></b>" % html_fail, html=True)
                    self.robot_env.log_to_console("5. PRODUCT WITH 'SONY' 'TV' WAS NOT LOCATED")
                    self.commonobj.get_screenshot(self.commonobj.driver, "Product List")
                self.commonobj.get_screenshot(self.commonobj.driver, "4_Product_Selection_Success")
        except Exception as e:
            self.robot_env.log_to_console("5. PRODUCT WITH 'SONY' 'TV' WAS NOT LOCATED" + str(e))
            logger.info("\t <b><h3> FAILED TO IDENTIFY PRODUCT WITH 'SONY' 'TV' : %s </h3></b>" % html_fail, html=True)
            self.commonobj.get_screenshot(self.commonobj.driver, "4_Product_Selection_Failed")
            self.commonobj.close_driver()
