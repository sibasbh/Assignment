import re
import ast
import os
import yaml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSuite(object):

    def __init__(self, testcasenum="000"):
        robot_env = BuiltIn()
        self.status = False

        self.nxt_btn = robot_env.get_variable_value('${Home_Page.nxt_btn}')
        self.search_br = robot_env.get_variable_value('${Home_Page.search_br}')
        self.result_kw = robot_env.get_variable_value('${Home_Page.results_kw}')
        self.inch_search = robot_env.get_variable_value('${Home_Page.inch_search}')
        self.itemimg = robot_env.get_variable_value('${Home_Page.itemimg}')
        self.itemtitle = robot_env.get_variable_value('${Home_Page.itemtitle}')
        self.url = robot_env.get_variable_value("${ebay_shopping_%s.url}" % (testcasenum))
        self.input_item = robot_env.get_variable_value("${ebay_shopping_%s.input_item}" % (testcasenum))

        self.cond_value = robot_env.get_variable_value('${Product_Detail_Page.cond_value}')
        self.price_value = robot_env.get_variable_value('${Product_Detail_Page.price_value}')
        self.prod_name = robot_env.get_variable_value('${Product_Detail_Page.prod_name}')
        self.seller_information_value = robot_env.get_variable_value('${Product_Detail_Page.seller_information_value}')
        self.add_cart = robot_env.get_variable_value('${Product_Detail_Page.add_cart}')
        self.ebay_logo = robot_env.get_variable_value('${Product_Detail_Page.ebay_logo}')
        self.prot_plan = robot_env.get_variable_value('${Product_Detail_Page.prot_plan}')
        self.thank_btn = robot_env.get_variable_value('${Product_Detail_Page.thank_btn}')


        self.ck_title = robot_env.get_variable_value('${Checkout_Page.ck_title}')
        self.condition_value = robot_env.get_variable_value('${Checkout_Page.condition_value}')
        self.Price_value_checkout = robot_env.get_variable_value('${Checkout_Page.Price_value_ckout}')
        self.produce_name = robot_env.get_variable_value('${Checkout_Page.produce_name}')
        self.sellinfo = robot_env.get_variable_value('${Checkout_Page.sellinfo}')

        pass