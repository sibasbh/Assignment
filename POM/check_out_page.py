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
from product_detail_page import ProduceDetails

html_pass = '<b style="color:green">PASS</b>'
html_fail = '<b style="color:red">FAIL</b>'

class ShoppingCart:
    def __init__(self,commonobj,objSuite):
        """
        """
        self.robot_env = BuiltIn()
        self.commonobj = commonobj
        self.objSuite = objSuite

    def shoppingcart_page_validation(self):
        """
        :Step 1 : From Shopping Cart page copy Condition , Price , Product name , Seller Info to a dictionary.
        :Step 2 : This information is required to compare these values with once captured in Product Detail page.
        :return: NONE
        """
        try:
            title_elem = self.commonobj.custom_driver_wait(self.objSuite.ck_title)
            cart = title_elem.text

            if 'Your eBay Shopping Cart' in cart:
                self.prod_detail1 = {}
                key1 = "Condition"
                key2 = "Price"
                key3 = "Produce Name"
                key4 = "Seller Information"

                cond_elem = self.commonobj.custom_element(self.objSuite.condition_value, 'xpath')
                value1 = cond_elem.text

                price_elem = self.commonobj.custom_element(self.objSuite.Price_value_checkout, 'xpath')
                value2 = str(price_elem.text).replace('US ', '')

                prod_elem = self.commonobj.custom_element(self.objSuite.produce_name, 'xpath')
                value3 = prod_elem.text

                sell_elem = self.commonobj.custom_element(self.objSuite.sellinfo, 'css')
                value4 = sell_elem.text

                self.prod_detail1[key1] = value1
                self.prod_detail1[key2] = value2
                self.prod_detail1[key3] = value3
                self.prod_detail1[key4] = value4

                logger.info("\t <b><h3>PRODUCT DETAILS CAPTURED FROM SHOPPING CART PAGE : %s </h2></b>" % html_pass, html=True)
                self.robot_env.log_to_console("9. PRODUCT DETAILS CAPTURED FROM SHOPPING CART PAGE")
                self.commonobj.get_screenshot(self.commonobj.driver, "8_CartValidation_Success")

        except Exception as e:
            self.robot_env.log_to_console("9. PRODUCT DETAILS NOT CAPTURED FROM SHOPPING CART PAGE" , str(e))
            logger.info("\t <b><h3>PRODUCT DETAILS NOT CAPTURED FROM SHOPPING CART PAGE : %s </h2></b>" % html_fail,
                        html=True)
            self.commonobj.get_screenshot(self.commonobj.driver, "8_CartValidation_Failed")
            self.commonobj.close_driver()


    def product_detail_validation(self, prod_detail):
        """
        Step 1 : Compare Product details taken from product Detail Page and Shopping Cart page.
        Step 2 : Ensure all the details matches.
        :param prod_detail: Dictionary Value taken from Product detail page.
        :return: NONE
        """
        try:
            flag = 0
            for keyOne in prod_detail:
                for keyTwo in self.prod_detail1:
                    if keyOne == keyTwo:
                        if prod_detail[keyOne] == self.prod_detail1[keyTwo]:
                            flag = flag + 1
                        else:
                            flag = flag
                        break
            if flag == 4:
                self.robot_env.log_to_console("10. ALL PARAMETERS FROM PRODUCT DETAIL AND SHOPPING CART MATCHES")
                logger.info("\t <b><h3>ALL PARAMETERS FROM PRODUCT DETAIL AND SHOPPING CART MATCHES : %s </h2></b>" % html_pass,
                            html=True)
            else:
                self.robot_env.log_to_console("10. ALL PARAMETERS FROM PRODUCT DETAIL AND SHOPPING CART DOES NOT MATCHES")
                logger.info("\t <b><h3> PARAMETERS FROM PRODUCT DETAIL AND SHOPPING CART DOES NOT MATCH : %s </h2></b>" % html_fail,
                            html=True)

        except Exception as e:
            self.robot_env.log_to_console("10. ALL PARAMETERS FROM PRODUCT DETAIL AND SHOPPING CART DOES NOT MATCHES" ,str(e))
            logger.info("\t <b><h3>PARAMETERS FROM PRODUCT DETAIL AND SHOPPING CART DOES NOT MATCH : %s </h2></b>" % html_fail,
                        html=True)
            self.commonobj.close_driver()