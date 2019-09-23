import sys
import os
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageobjects.baidu_page import baidu_page


with baidu_page() as test_page:
    test_page.click_search_button()
    test_page.input_product_name("M479")

    
