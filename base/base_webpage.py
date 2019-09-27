import time
from base.base_broswer import broswer_engine
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

# Selenium Locator map like selenium.webdriver.common.by
_LOCATOR_MAP = {'css': By.CSS_SELECTOR,
                'id_': By.ID,
                'name': By.NAME,
                'xpath': By.XPATH,
                'link_text': By.LINK_TEXT,
                'partial_link_text': By.PARTIAL_LINK_TEXT,
                'tag_name': By.TAG_NAME,
                'class_name': By.CLASS_NAME,
                }
        

class base_page(broswer_engine):
    """
    Base Page class that all page models can inherit from
    Contains Wrappers for common Selenium operations
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
   
    def __enter__(self):      
        self.open_browser()
        return self 

    def __exit__(self,*args):
        self.close_browser()

    def get_element(self,loc,element_driver = False,multi = False,wait_time =30):
        """Get the element/elements from web
         
        :param multi:  `bool`
            return elements or element
        :param loc: `dict`
            format: {'xpath':'//*'}
            support the locator in _LOCATOR_MAP
        :param wait_time: `int`
            Webdriver will wait for "wait_time" until the element is visible
    
        """

        if element_driver:
            _driver = element_driver
        else :
            _driver = self.driver
            
        loc_iter = iter(loc.items())
        k,v = next(loc_iter)
        self.locator = (_LOCATOR_MAP[k], v)
        print(self.locator)
        if multi:  
            try:
                WebDriverWait(_driver ,wait_time).until(EC.visibility_of(_driver.find_elements(*self.locator)[0]))
                return _driver .find_elements(*self.locator)
            except NoSuchElementException as e:
                raise ValueError('Invaild locator') from e          
        else:
            try:
                WebDriverWait(_driver,wait_time).until(EC.visibility_of(_driver.find_element(*self.locator)))
                return _driver .find_element(*self.locator)
            except NoSuchElementException as e:
                raise ValueError('Invaild locator') from e  

    def click_element(self,locator,element = None,wait_seconds = 2):
        """
        click the element then wait 
        """
        result_flag = False
        if not element :
            link =  self.get_element(locator)
        else:
            link = element
        try:
            if link is not None:
                self.driver.execute_script("arguments[0].scrollIntoView();", link)
                link.click()
                self.wait(wait_seconds)
        except Exception as e:
            print("click event error") 
        else:
            result_flag =True 
        finally:  
            return result_flag

    def set_text(self,locator,value,wait_seconds=2,clear_flag=True):
        """
        Clear the text field before filling in.
        """
        text_field = None
        try:
            text_field = self.get_element(locator)
            if text_field is not None and clear_flag is True:
                try:
                    text_field.clear()
                except Exception as e:
                    print("clear error")
        except Exception as e:
            print("set text find element loc error")
        
        result_flag = False
        if text_field is not None:
            try:
                text_field.send_keys(value)
                self.wait(wait_seconds)
            except Exception as e:
                print("text field error")
            else:
                result_flag =True 
            finally:  
                return result_flag

    def wait(self,wait_seconds=5,locator=None):
        """
        Performs wait for time provided
        """
        if locator is not None:
            self.smart_wait(wait_seconds,locator)
        else:
            time.sleep(wait_seconds)
        
    def smart_wait(self,wait_seconds,locator):

        """
        Performs an explicit wait for a particular element
        """
        result_flag = False
        try:
            WebDriverWait(self.driver, wait_seconds).until(EC.presence_of_element_located(locator))
        except Exception as e:
            print("wait error")
        else:
            result_flag =True 
        finally:  
            return result_flag

    def loc_split(self,raw_loc):
        return {raw_loc.split(",")[0].strip('"'):raw_loc.split(",")[1].strip('"')}