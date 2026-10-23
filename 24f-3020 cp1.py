import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# options = webdriver.ChromeOptions()
# options.add_argument("--incognito")

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com")
time.sleep(2)

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
loginBtn = driver.find_element(By.ID, "login-button")

time.sleep(3)
username.send_keys("standard_user")
password.send_keys("secret_sauce")
loginBtn.click()
time.sleep(3)

# opens up the item details Page
driver.find_element(By.ID, "item_1_title_link").click()
time.sleep(1)
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


#checkout condition
if "checkout-complete" in driver.current_url:
    print(f" order is placed successfully!")
else:
    print(f"Failed to place an order")

time.sleep(5)
driver.quit() 
