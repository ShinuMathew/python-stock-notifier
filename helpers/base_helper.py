from bs4 import BeautifulSoup
from enums.enums import Stock, Status
from helpers.redis_helper import RedisHelper
from helpers.smtp_helper import *
import requests, json, re
import redis

class BaseHelper:

    def __init__(self):
        self.config = self._loadConfig()
        self.redis = RedisHelper()

    # Load data from config
    def _loadConfig(self):
        print("\n ==> LOAD DATA FROM CONFIG ")
        with open('./config.json', 'r') as configJson:
            config = json.load(configJson)
        print("Loaded data from config...")
        return config

    # Make request
    def makeRequest(self):
        print("\n ==> MAKE REQUEST TO AMAZON ")
        URL = self.config["base_url"]
        # To get user agent simply search my user agent in google
        headers = {"User-Agent": self.config["user_agent"]}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        print("Request successfully made to amazon...")
        return soup

    # Get product title
    def getProductTitle(self, soup):
        print("\n ==> GET PRODUCT TITLE ")    
        title = str(soup.find(id=self.config["elements"]["product_title"]["target_value"])
                .get_text()).replace("\s", "")
        print("Product title : "+title)
        return title

    # Get product stock
    def getProductStock(self, soup):
        print("\n ==> GET PRODUCT STOCK ")
        stock_text = str(re.search('[^\s][a-zA-Z\s]{7,30}', 
                soup.find(id=self.config["elements"]["stock_text"]["target_value"]).get_text())
                .group(0).replace('.', '')).replace(" ", "")
        print("Product Stock : "+stock_text)
        return stock_text

    # Get product price
    def getProductPrice(self, soup):
        print("\n ==> GET PRODUCT PRICE ")
        # price_text = price_text.encode('ascii','ignore')
        price = str(re.search('[\d,.]{1,9}[^\s]', 
                soup.find(id=self.config["elements"]["price_text"]["target_value"]).get_text())
                .group(0).replace(",", ""))
        print("Product Price : "+price)    
        return float(price)

    # Get product price to cache
    def _getProductPrice(self, currentProductPrice):
        oldProductPrice = self.redis.getData("product_price")
        if(oldProductPrice == None):
            self.redis.setDataWithExp("product_price", currentProductPrice, 60*3)
            return currentProductPrice
        else:
            return float(oldProductPrice)

    # Get product price from cache and compare price
    def getAndComparePrice(self, currentProductPrice):
        oldProductPrice = self._getProductPrice(currentProductPrice)
        if(currentProductPrice < oldProductPrice):
            print("Success!! Price decrease observed. Its a good time to order :)")
            return Status.SUCCESS
        else:
            print("Price still seems to be up :( ... Not a good time to order")
            return Status.FAILURE