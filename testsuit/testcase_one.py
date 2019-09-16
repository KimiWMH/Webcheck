import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageobjects.guide_page import guide_page


with guide_page() as test_page:
    test_page.input_product_name("M479")
    test_page.click_search_button()
