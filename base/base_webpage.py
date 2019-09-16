import time
from base.base_broswer import broswer_engine
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class base_page(broswer_engine):
    """
    Base Page class that all page models can inherit from
    Contains Wrappers for common Selenium operations
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_element(self,loc,wait_time = 60):
        WebDriverWait(self.driver,wait_time).until(EC.visibility_of(self.driver.find_element_by_xpath(loc)))
        return self.driver.find_element_by_xpath(loc)

    def click_element(self,locator,wait_seconds = 2):
        """
        click the element then wait 
        """
        result_flag = False
        try:
            link =  self.get_element(locator)
            if link is not None:
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