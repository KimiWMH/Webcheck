import os
import time
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base.base_webpage import base_page


class guide_page(base_page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __enter__(self):      
        self.open_browser()
        return self 

    def __exit__(self,*args):
        self.close_browser()

    def input_product_name(self,input_text):   
        locator_input_searchbox = (r"//div[@id = 'printerPfinderContainer']//input[@id = 'search-input-pfinder']")
        assert self.set_text(locator_input_searchbox,input_text) 

    def click_search_button(self):
        locator_button_submit = (r"//div[@id ='printerPfinderContainer']//button[@id = 'btnSplitSearchSubmit']")
        assert self.click_element(locator_button_submit)

if __name__ == "__main__":
    with guide_page() as test_page:
        test_page.input_product_name("M479")
        test_page.click_search_button()
