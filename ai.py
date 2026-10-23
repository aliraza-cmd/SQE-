import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Setup Chrome Options to run in Incognito Mode 
# (This completely stops Chrome's password leak alerts without needing new imports)
options = webdriver.ChromeOptions()
options.add_argument("--incognito")

# Start the browser with our hidden settings
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# 2. Open the practice e-commerce website
driver.get("https://saucedemo.com")
time.sleep(2)

# 3. Log into the system using default testing credentials
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# 4. Add the "Sauce Labs Bolt T-Shirt" to your cart [1]
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
print("👕 T-Shirt successfully added to cart!")
time.sleep(1)

# 5. Click the shopping cart icon to view selected items
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(2)

# 6. Click the checkout button to initiate order processing
driver.find_element(By.ID, "checkout").click()
time.sleep(2)

# 7. Complete the checkout information form
driver.find_element(By.ID, "first-name").send_keys("Ali")
driver.find_element(By.ID, "last-name").send_keys("Raza")
driver.find_element(By.ID, "postal-code").send_keys("38000")
driver.find_element(By.ID, "continue").click()
time.sleep(2)

# 8. Submit the order by clicking the final "Finish" button
driver.find_element(By.ID, "finish").click()
time.sleep(2)

# 9. Verify order success using the URL tracking method you learned
if "checkout-complete" in driver.current_url:
    print("🎉 SUCCESS: Your order has been placed seamlessly without any alerts!")
    confirmation_text = driver.find_element(By.CLASS_NAME, "complete-header").text
    print(f"Website Confirmation Message: {confirmation_text}")
else:
    print("❌ FAILED: Something unexpected went wrong during checkout.")

# 10. Manual window override
# This keeps the browser from closing by waiting for your input in the terminal console
input("\nThe process is complete! When you are ready to close the window, press ENTER in your terminal...")
driver.quit()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Setup Chrome Options to run in Incognito Mode 
# (This completely stops Chrome's password leak alerts without needing new imports)
options = webdriver.ChromeOptions()
options.add_argument("--incognito")

# Start the browser with our hidden settings
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# 2. Open the practice e-commerce website
driver.get("https://saucedemo.com")
time.sleep(2)

# 3. Log into the system using default testing credentials
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# 4. Add the "Sauce Labs Bolt T-Shirt" to your cart [1]
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
print("👕 T-Shirt successfully added to cart!")
time.sleep(1)

# 5. Click the shopping cart icon to view selected items
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(2)

# 6. Click the checkout button to initiate order processing
driver.find_element(By.ID, "checkout").click()
time.sleep(2)

# 7. Complete the checkout information form
driver.find_element(By.ID, "first-name").send_keys("Ali")
driver.find_element(By.ID, "last-name").send_keys("Raza")
driver.find_element(By.ID, "postal-code").send_keys("38000")
driver.find_element(By.ID, "continue").click()
time.sleep(2)

# 8. Submit the order by clicking the final "Finish" button
driver.find_element(By.ID, "finish").click()
time.sleep(2)

# 9. Verify order success using the URL tracking method you learned
if "checkout-complete" in driver.current_url:
    print("🎉 SUCCESS: Your order has been placed seamlessly without any alerts!")
    confirmation_text = driver.find_element(By.CLASS_NAME, "complete-header").text
    print(f"Website Confirmation Message: {confirmation_text}")
else:
    print("❌ FAILED: Something unexpected went wrong during checkout.")

# 10. Manual window override
# This keeps the browser from closing by waiting for your input in the terminal console
input("\nThe process is complete! When you are ready to close the window, press ENTER in your terminal...")
driver.quit()
