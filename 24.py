
import unittest                                                                                                            
from selenium import webdriver                                                                                             
from selenium.webdriver.chrome.options import Options                                                                      
import requests                                                                                                            
# using time should be probably replaced by some advanced method                                                           
import time                                                                                                                
                                                                                         
                                                                                                                           
                                                                                                                           
chrome_options = Options()                                                                                                 
chrome_options.add_argument("--ignore-certificate-errors")                                                                 
chrome_options.add_argument("--incognito")                                                                                 
                                                                                                                           
# website to be tested url                                                                                                 
url = "http://somewebsite.com"                                                                                             
# url = "http://www.google.com/"                                                                                           
                                                                                                                           
# if you need browser to be opened change headless to False                                                                
headless = True                                                                                                            
#headless = False                                                                                                          
                                                                                                                           
# company_specific_div_id                                                                                                  
# это какой-то id у div , который мы точно ожидаем найти перейдя на сайт                                                   
# чтобы проверить попали мы куда надо или нет                                                                              
                                                                                                                           
company_specific_div_id = "someId-12345"                                                                                   
                                                                                                                           
# main page text - to use for successful login assertion                                                                   
# этот текст появляется на главной странице после успешного логина.                                                        
# будем использовать его, что проверить залогинились мы или нет                                                            
                                                                                                                           
main_page_text = "You have logged in to somewebsite.com"                                                                  
                                                                                                                           
                                                                                                                           
class TestSomeWebsite(unittest.TestCase):                                                                                  
    @classmethod                                                                                                           
    def setUpClass(inst):                                                                                                  
        # create a new Chrome session                                                                                      
        inst.headless = headless                                                                                           
        chrome_options = Options()                                                                                         
        if headless == True:                                                                                               
            chrome_options.add_argument("--headless")                                                                      
            chrome_options.add_argument("--kiosk")                                                                         
            print("Running in headless mode")                                                                              
        else:                                                                                                              
            print("Running head over hills")                                                                               
                                                                                                                           
        inst.driver = webdriver.Chrome(options=chrome_options)                                                             
        inst.driver.implicitly_wait(30)                                                                                    
        inst.driver.maximize_window()                                                                                      
        # navigate to the application home page                                                                            
        inst.driver.get(url)                                                                                               
        inst.driver.title                                                                                                  
                                                                                                                           
    def test_company_div_exists(self):                                                                                     
        self.company_div_to_test = company_specific_div_id                                                                 
                                                                                                                           
        def check_that_div_exists(self,company_div):                                                                       
            self.company_div = company_div                                                                                 
            try:                                                                                                           
                self.driver.find_element_by_id(company_div)                                                                
            except:                                                                                                        
                print("\nelement not found")                                                                               
                return False                                                                                               
            return True                                                                                                    
                                                                                                                           
        self.assertTrue(check_that_div_exists(self, self.company_div_to_test))                                             
                                                                                                                           
                                                                                                                           
    def test_login(self):                                                                                                  
                                                                                                                           
        array = self.driver.find_elements_by_class_name("v-textfield")                                                     
        print(array[0])                                                                                                    
        array[0].send_keys("userName")                                                                                     
        array[1].send_keys("password")                                                                                     
        buttons = self.driver.find_elements_by_class_name("v-button")                                                      
        print(buttons[0])                                                                                                  
        lbutton = buttons[0]                                                                                               
        print(lbutton)                                                                                                     
        lbutton.click()                                                                                                    
                                                                                                                           
        def check_that_driver_logged_in(self,text_for_assertion):                                                          
            self.text_for_assertion = text_for_assertion                                                                   
            try:                                                                                                           
               homePageText = self.driver.find_element_by_xpath(f"//*[text()='{text_for_assertion}']")              
            except:                                                                                                        
                print("\nHH check_that_driver_logged_in function ERROR: Text not found, probably login failed")            
                return False                                                                                               
            return True                                                                                                    
                                                                                                                           
        self.assertTrue(check_that_driver_logged_in(self,main_page_text), "HH ASSERTION ERROR COMMENT: Text not found")    
                                                                                                                           
                                                                                                                           
    @classmethod                                                                                                           
    def tearDownClass(inst):                                                                                               
        time.sleep(1)                                                                                                      
        # close the browser window                                                                                         
        inst.driver.quit()                                                                                                 
                                                                                                                           
if __name__ == '__main__':                                                                                         
    unittest.main()                                                                                                        
    
