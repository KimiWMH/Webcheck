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

def test_case(product_name,os_platform,os_version):        
    dict = {
        'driver_link': '', 
        'driver_name': '', 
        'driver_type': 'Skip', 
        'os_platform': os_platform,
        'os_version': os_version, 
        'produc_name': product_name
        }
    c = []

    with test_page() as tp:
        tp.input_product_name("M479")
        tp.click_search_button()
        tp.os_switch(os_platform,os_version)
        tp.click_open_close_all_button()
        k= tp.get_panel_title()

    for i in k:    
        c.append(dict)
        for item in k[::2]:
            c[-1]['driver_link'] = item
        for item  in k[1::2]:
            c[-1]['driver_name'] = item

    return c 

if __name__ == "__main__":
    
    capture_data =test_case("M479","Windows",r"Windows 8 (64-bit)")
    verify_data = get_test_data()
    p.pprint(verify_data)
    for i,v in enumerate(capture_data):
        p.pprint(v)
        if v in verify_data:
            print("PSA")
        else:
            p.pprint("FAIL")