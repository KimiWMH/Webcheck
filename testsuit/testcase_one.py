import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageobjects.guide_page import guide_page
from pageobjects.product_page import product_page
from data.data import get_test_data
import pprint as p

class test_page(product_page,guide_page):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)


if __name__ == "__main__":
    with test_page() as tp:
        # tp.input_product_name("M479")
        # tp.click_search_button()
        # tp.os_switch("SAP","SAP")
        # p,v = tp.get_os_list_context()
        # print(p)
        # print(v)
        tp.click_open_close_all_button()
        g= tp.get_panel_title()
        p.pprint(g)
       

