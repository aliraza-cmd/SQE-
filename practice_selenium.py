from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")
userNameField = driver.find_element(By.ID, "username")
pwdField = driver.find_element(By.ID, "password")
submitBtn= driver.find_element(By.ID, "submit")

#entering credentials

userNameField.send_keys("student")
pwdField.send_keys("Password123")


time.sleep(3)
#clicking the button
submitBtn.click()

# After clicking the submit button and waiting a few seconds...
if "login" not in driver.current_url:
    print("Success! The URL changed, meaning you are logged in.")
else:
    print("Failed! You are still on the login page.")



time.sleep(10)
driver.quit()



