import time
import json

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class EasyApply:
    

    def __init__(self, data):
        """Parameter initiliazation
        
        Args:
            data: A config.json file
        """
        self.username = data['username']
        self.password = data['password']
        self.url = data['url']
        self.driver = webdriver.Chrome(data['driver_path'])
    

    def login(self):
        """Login to NYC Housing Website"""
        self.driver.get(self.url)
        username_textbox = self.driver.find_element_by_id("Username")
        username_textbox.send_keys(self.username)
        password_textbook = self.driver.find_element_by_id("Password")
        password_textbook.send_keys(self.password)
        login_butt = self.driver.find_element_by_name("button")
        login_butt.click()
        # wait for page to load before clicking log in 
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log In"))
            )
            element.click()
        except:
            self.driver.quit()

 
    def open_lotteries(self):
        """Click on Open Lotteries page"""       
        element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Open Lotteries")))
        element.click()


    def find_offers(self):
        """Find all offers on current page"""
        url1 = "https://housingconnect.nyc.gov/PublicWeb/search-lotteries"
        self.driver.get(url1)
        time.sleep(10)
        total_results = self.driver.find_elements_by_class_name("card")
        print("test")
        for i in range(0, len(total_results)):
            self.driver.get(url1)
            time.sleep(10)
            total_results = self.driver.find_elements_by_class_name("card")
            total_results[i].click()
            print("clicked the {}".format(i))
            time.sleep(20)

            #check if already applied.
            check = self.driver.find_element_by_xpath('//*[@id="howtoapply"]'
                                                '/div/div/div[3]/div/a').text
            if check == "Applied":
                print("already applied")
                self.driver.back()
                time.sleep(10)
                continue
            #new house, apply
            else:
                print("applying")
                self.driver.find_element_by_link_text("Apply Now").click()
                time.sleep(5)
                self.driver.find_element_by_class_name("mat-checkbox-inner-container").click()
                print("clicked the check box")
                time.sleep(5)
                try:
                    self.driver.find_element_by_xpath('//*[@id="apply-section"]/div/div[2]/div/div/div/div/div[3]/div[2]/button[1]').click()
                except:
                    self.driver.find_element_by_class_name("fade-in").click()
                print("clicked submit")
                time.sleep(3)
                print("return to previous page")
                self.driver.back()
                time.sleep(5) 
                continue
    

    def sort_by_expiring_soonest(self):
        """sort page by expiring soonest"""
        print('test') 


   # def submit_appply(self, ):
        

if __name__ == '__main__':
    with open('config.json') as config_file:
        data = json.load(config_file)
    bot = EasyApply(data)
    bot.login()
    time.sleep(10)
    bot.open_lotteries()
    time.sleep(10)
    bot.find_offers()
    time.sleep(2)
