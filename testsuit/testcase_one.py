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
        # platform,version = tp.get_os_list_context()
        
        # print(platform)
        # print(version)

        # verify_data = get_test_data()
        # for data in verify_data:
        #     try:
        #         print(platform.index(data['os_platform']))       
        #     except:
        #         print(data['os_platform'])
        #     try:
        #         print(platform.index(data['os_version']))                
        #     except:
    #             print(data['os_version'])
        tp.click_open_close_all_button()
        #k = tp.get_panel_title()
        k = tp.get_hiden_downlink()
        print(k)
        # for t in k[::2]:
        #     p.pprint(t)
        # for t in k[1::2]:
        #     p.pprint(t)   
    
    # verify_data = get_test_data()
    # for data in verify_data:
    #     # assert platform.index(data['os_platform'])
    #     # assert version.index(data['os_version'])
    #     print(data['os_platform'])      
    #     print(data['os_version'])      
