from object import Product
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

shopping = Product()
shopping.openSite("https://www.saucedemo.com")
shopping.Login("standard_user", "secret_sauce")
shopping.processShop("item_1_title_link")
shopping.isCompleted()
shopping.endBrowser()