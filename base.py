from bs4 import BeautifulSoup
from enums.stock import Stock, Status
from helpers.smtp_helper import *
from helpers.base_helper import BaseHelper
import requests, json, re
import redis


class Base:
    def __init__(self):
        self.URL = ""
        self.headers = {}
        self.expectedPrice = 46999
        self.baseHelper = BaseHelper()


    def start(self):
        soup = self.baseHelper.makeRequest()
        title = self.baseHelper.getProductTitle(soup)
        stock_text = self.baseHelper.getProductStock(soup)
        if(stock_text == Stock.INSTOCK.value):
            print("Your product is instock.... Verifying if any price decrease...")
        price = self.baseHelper.getProductPrice(soup)
        # Price static value to be replaced from the one from redis cache
        status = self.baseHelper.getAndComparePrice(price)
        if(status.value == Status.SUCCESS.value):
            print("Sending mail....")


Base().start()