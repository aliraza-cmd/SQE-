from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Product:
    def __init(self, driver):
        self.driver = webdriver.Chrome()
        
        
    def openSite(self, link):
        driver.get(link)
        
    def Login(self, user, pwd):
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        loginBtn = driver.find_element(By.ID, "login-button")
        time.sleep(3)
        username.send_keys(user)
        password.send_keys(pwd)
        loginBtn.click()
        time.sleep(3)
        
    def findElement(self, productId):
        driver.find_element(By.ID, productID).click()
        time.sleep(1)
    def processShop(self, productID):
    
        productBtn = driver.find_element(By.ID, "add-to-cart")
        time.sleep(2)
        productBtn.click()
        shoppingCart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        time.sleep(3)
        shoppingCart.click()
        time.sleep(2)

        checkOutBtn = driver.find_element(By.ID, "checkout")
        time.sleep(3)
        checkOutBtn.click()
        
        #  fake details
        driver.find_element(By.ID, "first-name").send_keys("Ali")
        driver.find_element(By.ID, "last-name").send_keys("Raza")
        driver.find_element(By.ID, "postal-code").send_keys("3020")

        time.sleep(2)
        driver.find_element(By.ID, "continue").click()

        finishBtn = driver.find_element(By.ID, "finish")
        finishBtn.click()
        time.sleep(3)
        
        
    def isCompleted(self, condition):
        if condition in driver.current_url:
            print(f" order is placed successfully!")
        else:
            print(f"Failed to place an order")
    
    def endBrowser():
        driver.quit()
            
            

shopping = Product(webdriver.Chrome())
shopping.openSite("https://www.saucedemo.com")
shopping.processShop("item_1_title_link")
shopping.isCompleted()
shopping.endBrowser()

