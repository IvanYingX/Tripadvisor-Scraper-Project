from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
#hotel_links =[]
class ScrapUrl():
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    
    def web_driver(self, URL: str)-> None:
        """get webdriver to pointing website

        Args:
            URL (str): url of website

        
        """
        self.driver.get(URL)

    def accept_cookies_button(self, xpath : str) ->None:
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
    

    def search_city(self, city : str, xpath : str)-> None:

        """Search city
        # xpath of searchbar : //*[@id="onetrust-accept-btn-handler"]
        Args:
            
            xpath (str): xpath of searchBar 
            city (str): Name of city to search in search bar
        """
        time.sleep(3)
        serch_section = self.driver.find_element_by_xpath(xpath)
       

        serch_section.send_keys(Keys.RETURN)
        serch_section.send_keys(city)
        serch_section.send_keys(Keys.RETURN)

    def hotel_tab(self, xpath_hotel_tab: str) -> None:
        """travser to hotel tab

        Args:
            xpath_hotel_tab (str): xpath of hotel tab
        """
        time.sleep(3)
        self.driver.find_element_by_xpath(xpath_hotel_tab).click()

    def get_urls_of_Hotel(self, xpath_hotel: str)-> list:
        """Get url of all hotel

        Args:
            
            xpath_hotel (str): xpath of hotel '//a[@class = "review_count"]'
            
        """
        time.sleep(3)
        
        hotel_links =[]
        for i in range(1,6):
            
            list_hotels = self.driver.find_elements_by_xpath(xpath_hotel)
            for i in range(len(list_hotels)):
                link = (list_hotels[i].get_attribute('href')).replace("#REVIEWS","")
                hotel_links.append(link)
            
            # next page button click
            self.driver.find_element_by_link_text("Next").click()
            
            len(hotel_links) 
            time.sleep(5)
        
        return hotel_links

  

    def get_hotel_data(self, hotellist : list)-> dict:
        """get hotel information, and ameneties
        Args:
            hotellist (list): list of hotels
        """

        hotel_info = {"name":[],"address":[], "reviews":[], "mail_id":[],"rating": [],"amenities": []}
        

        for i in range(len(hotellist)):
            time.sleep(3)
            self.driver.get(hotellist[i])
            try:
                hotel_name = self.driver.find_element_by_xpath('//h1[@id = "HEADING"]').text

                
            except:
                hotel_name = ""
            hotel_info["name"].append(hotel_name)
            

            try:
                hotel_address = self.driver.find_element_by_xpath('//div[@class = "ewock"]').text
            except:
                hotel_address = ""
            hotel_info["address"].append(hotel_address)
            


            try:
                hotel_reviews = self.driver.find_element_by_xpath('//span[@class="HFUqL"]').text
            except:
                hotel_reviews = ""    
            hotel_info["reviews"].append(hotel_reviews)
            

            '''try:
                hotel_phone = self.driver.find_element_by_xpath('//div[@class="fdbDs"]').text
            except:
                hotel_phone = ""
            hotel_info["phone"].append(hotel_phone)
            print(hotel_phone)
            '''

            try:
                hotel_mail_id = self.driver.find_element_by_xpath('//a[@class = "bIWzQ fWKZw"]').get_attribute('href')
            except:
                hotel_mail_id = ""
            hotel_info["mail_id"].append(hotel_mail_id)
            print(hotel_mail_id)


            try:
                hotel_rating = self.driver.find_element_by_xpath('//span[@class="bvcwU P"]').text
            except:
                hotel_rating = ""
            hotel_info["rating"].append(hotel_rating)
            print(hotel_rating)

            amenities = self.driver.find_elements_by_xpath('//div[@class="bUmsU f ME H3 _c"]')
            property_amenities = []
            for i in range(len(amenities)):
                amenity = amenities[i].text
                if amenity != '':
                    property_amenities.append(amenity)
            hotel_info["amenities"].append(list(set(property_amenities)))
            

        
        return hotel_info






def scrap():
    obj = ScrapUrl()
    obj.web_driver("https://www.tripadvisor.co.uk/")
    obj.accept_cookies_button('//*[@id="onetrust-accept-btn-handler"]')
    obj.search_city('London', '//*[@id="lithium-root"]/main/div[3]/div/div/div[2]/form/input[1]')
    obj.hotel_tab('//*[@id="search-filters"]/ul/li[2]/a')
    hotel_links = obj.get_urls_of_Hotel('//a[@class = "review_count"]')
    hotel_data_dict =obj.get_hotel_data(hotel_links)
    
if __name__ == '__main__':
    scrap()