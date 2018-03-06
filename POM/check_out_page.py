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
from robot.utils.asserts import *


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
        self.prod_detail1 = {}
        key1 = "Condition"
        key2 = "Price"
        key3 = "Produce Name"
        key4 = "Seller Information"
        value1 = self.commonobj.custom_element(self.objSuite.condition_value, 'xpath').text
        assert_not_none(value1, "Unable to capture Condition")
        price_elem = self.commonobj.custom_element(self.objSuite.Price_value_checkout, 'xpath')
        value2 = str(price_elem.text).replace('US ', '')
        assert_not_none(value2, "Unable to capture the Price")
        value3 = self.commonobj.custom_element(self.objSuite.produce_name, 'xpath').text
        assert_not_none(value3, "Unable to capture the Product Name")
        value4 = self.commonobj.custom_element(self.objSuite.sellinfo, 'css').text
        assert_not_none(value4, "Unable to capture the Product Name")

        self.prod_detail1[key1] = value1
        self.prod_detail1[key2] = value2
        self.prod_detail1[key3] = value3
        self.prod_detail1[key4] = value4

        self.robot_env.log_to_console("Shopping Cart - Captured Product Informations")
        return self.prod_detail1

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
            return flag
        except Exception as e:
            self.robot_env.log_to_console("Element not found :" + str(e))
            return False
