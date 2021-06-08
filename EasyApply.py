from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import json

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

class EasyApply:
    def __init__(self, data):
        self.username = data['username']
        self.password = data['password']
        self.url = data['url']
        self.driver = webdriver.Chrome(data['driver_path'])
   

    def login(self):
        # THIS FUNCTION LOGS INTO NYC HOUSING PROFILE  
        self.driver.get(self.url)
        username_textbox = self.driver.find_element_by_id("Username")
        username_textbox.send_keys(self.username)
        password_textbook = self.driver.find_element_by_id("Password")
        password_textbook.send_keys(self.password)
        login_butt = self.driver.find_element_by_name("button")
        login_butt.click()
       
        # WAIT FOR PAGE TO LOAD BEFORE CLICKING  
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT,"Log In"))
            )
            element.click()
        except:
           self.driver.quit() 

    def Open_Lotteries(self):
        # GOES TO OPEN LOTTERY PAGE
        element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT,"Open Lotteries"))
        )
        element.click()
    def find_offers(self):
        #This functions finds all the houses through all pages
        # find the total amount of results 
        total_results = self.driver.find_element_by_class_name("card-container")
        print(total_results)

    def store_houses(self):
        #grabs data of current houses and store into a csv
        current_url = self.driver.current_url
        self.driver.get(current_url)
        time.sleep(3)
        page = self.driver.page_source
        soup = soup(page, 'html.parser')
        container = soup.find_all('div')
        print(container)
if __name__ == '__main__':
    with open('config.json') as config_file:
        data = json.load(config_file)
    bot = EasyApply(data)
    bot.login()
    bot.Open_Lotteries()
    time.sleep(2)
    bot.find_offers()
    time.sleep(2)
    bot.store_houses()
    bot2 = EasyApply(data2)

