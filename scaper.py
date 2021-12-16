from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

class ScrapUrl():
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    
    def webDriver(self, URL: str)-> None:
        """get webdriver to pointing website

        Args:
            URL (str): url of website

        
        """
        self.driver.get(URL)

    def acceptCookiesButton(self, xpath : str) ->None:
        """accept cookies button
        # xpath of accept button  : //*[@id="onetrust-accept-btn-handler"]
        Args:
            
            xpath (str): xpath of cookies accept Button
        """

        #driver.get(URL)
        time.sleep(3)
        try:
            cookies_btn = self.driver.find_element_by_xpath(xpath)
            cookies_btn.click()
        except:
            print(cookies_btn.text)
    

    def searchCity(self, xpath : str, city : str)-> None:

        """accept cookies button
        # xpath of accept button  : //*[@id="onetrust-accept-btn-handler"]
        Args:
            
            xpath (str): xpath of searchBar 
            city (str): Name of city to search in search bar
        """
        time.sleep(3)
        serch_section = self.driver.find_element_by_xpath(xpath)
        #serch_section.
        #serch_section.text
        #actions = ActionChains(driver)
        #actions.move_to_element(serch_section).send_keys("London")
        # xpath of search bar : //*[@id="lithium-root"]/main/div[3]/div/div/div[2]/form/input[1]

        serch_section.send_keys(Keys.RETURN)
        serch_section.send_keys(city)
        serch_section.send_keys(Keys.RETURN)

    def getUrlssofHotel(self,xpath_hotel_tab: str, xpath_hotel:str, xpath_nextbutton: str)-> None:
        """Get url of all hotel

        Args:
            xpath_hotel_tab (str): xpath of hetel tab
            xpath_hotel (str): xpath of hotel
            xpath_nextbutton (str): xpath of next button
        """
        time.sleep(3)
        hotels_tab = self.driver.find_element_by_xpath(xpath_hotel_tab).click()
        hotel_links =[]
        for i in range(1,6):
            
            list_hotels = self.driver.find_elements_by_xpath(xpath_nextbutton)
            for i in range(len(list_hotels)):
                link = (list_hotels[i].get_attribute('href')).replace("#REVIEWS","")
                hotel_links.append(link)
                print(link)

            
            #hotel_links += list_hotels

            #len(hotel_links)    
            
            next_page = self.driver.find_element_by_xpath('//a[@class = "ui_button nav next primary "]')
            print(next_page.text, i)
            next_page.click()
            len(hotel_links) 
            time.sleep(5)

''' # TO DO: 
    def nextPage(self, xpath:str)-> None:

        """ for traverse to the next page of website
        # xpath of next page button : //a[@class = "ui_button nav next primary "]
        Args:
            driver (webdriver): webdrive
            xpath (str): xpath of next button
        """
        next_page = self.driver.find_element_by_xpath(xpath)
        next_page.click()
'''     

