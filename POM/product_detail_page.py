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
            if search_elem.is_displayed():
                self.prod_detail = {}
                key1 = "Condition"
                key2 = "Price"
                key3 = "Produce Name"
                key4 = "Seller Information"

                cond_elem = self.commonobj.custom_element(self.objSuite.cond_value, 'xpath')
                value_1 = cond_elem.text

                price_elem = self.commonobj.custom_element(self.objSuite.price_value, 'xpath')
                value_2 = str(price_elem.text).replace('US ','')

                prod_elem = self.commonobj.custom_element(self.objSuite.prod_name, 'xpath')
                value_3 = prod_elem.text

                sell_elem = self.commonobj.custom_element(self.objSuite.seller_information_value, 'xpath')
                value_4 = sell_elem.text

                self.prod_detail[key1] = value_1
                self.prod_detail[key2] = value_2
                self.prod_detail[key3] = value_3
                self.prod_detail[key4] = value_4

                self.robot_env.log_to_console("6. PROD DETAIL PAGE - CAPTURED PRODUCT INFORMATION")
                logger.info("\t <b><h3> PROD DETAIL PAGE - CAPTURED PRODUCT INFORMATION : %s </h3></b>" % html_pass,html=True)
                self.commonobj.get_screenshot(self.commonobj.driver, "5_Product_Detail_validation_Success")
                return self.prod_detail

        except Exception as e:
            self.robot_env.log_to_console("6. PROD DETAIL PAGE - CAPTURED PRODUCT INFORMATION FAILED :" , str(e))
            logger.info("\t <b><h3> PROD DETAIL PAGE - FAILED TO CAPTURED PRODUCT INFORMATION : %s </h3></b>" % html_fail,html=True)
            self.commonobj.get_screenshot(self.commonobj.driver, "5_Product_Detail_validation_Failed")
            self.commonobj.close_driver()


    def validate_condition_parameter(self):
        """
        Step 1 : From dictionary created from product_detail_page validate if Condition Parameter is Empty.
        Step 2 : Condition parameter should Not be empty
        :return: NONE
        """
        try:
            for key, value in self.prod_detail.items():
                if key == 'Condition':
                    if value is None or value == '':
                        logger.info(
                            "\t <b><h3> PROD DETAIL PAGE- CONDITION IS EMPTY : %s </h3></b>" % html_fail,html=True)
                        self.robot_env.log_to_console("7. CONDITION IS EMPTY")
                    else:
                        logger.info("\t <b><h3> PROD DETAIL PAGE- CONDITION IS NOT EMPTY : %s </h2></b>" % html_pass, html=True )
                break
            cart_elem = self.commonobj.custom_element(self.objSuite.add_cart, 'xpath')
            cart_elem.click()
            self.commonobj.get_screenshot(self.commonobj.driver, "6_AddToCart_Launch_Success")
        except Exception as e:
            self.robot_env.log_to_console("7. CONDITION IS EMPTY" , str(e))
            self.commonobj.get_screenshot(self.commonobj.driver, "6_AddToCart_Launch_Failed")
            logger.info("\t <b><h3> PROD DETAIL PAGE- CONDITION IS EMPTY : %s </h3></b>" % html_fail, html=True)
            self.commonobj.close_driver()




    def protection_plan(self):
        """
        Step 1: Handle Protection Plan page if it appears.
        Step 2: Tap on 'No Thanks' button if Protection Plan page appears.
        :return: NONE
        """
        try:
            if (self.commonobj.custom_element(self.objSuite.prot_plan, 'xpath') != None):
                thank_elem = self.commonobj.custom_element(self.objSuite.thank_btn, 'xpath')
                self.commonobj.custom_click(thank_elem, "No Thanks")
                self.commonobj.get_screenshot(self.commonobj.driver, "7_Protection Plan")
                self.robot_env.log_to_console("8. PROTECTION PLAN PAGE IS HANDLED")
                logger.info("\t <b><h3> PROTECTION PLAN PAGE IS HANDLED : %s </h3></b>" % html_pass, html=True)
                self.commonobj.get_screenshot(self.commonobj.driver, "7_ProductDetailPage_Success")
            else:
                self.robot_env.log_to_console("8. PROTECTION PLAN PAGE IS SKIPPED")
                pass
        except Exception as e:
            self.robot_env.log_to_console("8 . PROTECTION PLAN NOT HANDLED PROPERLY : ", str(e))
            self.commonobj.get_screenshot(self.commonobj.driver, "7_ProductDetailPage_Failed")
            self.commonobj.close_driver()
