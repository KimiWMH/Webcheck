import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageobjects.guide_page import guide_page
from pageobjects.product_page import product_page

class test_page(product_page,guide_page):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

with test_page() as tp:
    tp.input_product_name("M479")
    tp.click_search_button()
    tp.click_open_close_all_button()
    tp.os_switch("SAP","SAP")
    tp.wait(20)