import sys
import os
import time
import pytest 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageobjects.baidu_page import baidu_page

class test_page(baidu_page):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

class Test_Web_Data():
    @pytest.mark.skip(reason="Test Pytest Structure")
    @pytest.mark.parametrize("product_name",["M479"])
    def test_case(self,product_name):
        with baidu_page() as test_page:
            test_page.click_search_button()
            test_page.input_product_name(product_name)


    
