# from selenium import webdriver
# from selenium.webdriver.common.by import By



# driver = webdriver.Chrome()
# driver.get("https://flexstudent.nu.edu.pk/Login")
# text_box = driver.find_element(By.ID, "m_inputmask_4")

# text_box.send_keys("Ali Raza")
# submit_button = driver.find_element(
# By.CSS_SELECTOR, "button"
# )

# submit_button.click()


# print("TEST PASSED: Form submitted successfully!")

# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://flexstudent.nu.edu.pk/Login")
username = driver.find_element(By.ID, "m_inputmask_4")
pwd = driver.find_element(By.ID, "pass")
submit_button = driver.find_element(By.ID, "m_login_signin_submit")
username.send_keys("24F3020")
pwd.send_keys("AliRaza@3020")



print("Waiting for captcha to load...")
time.sleep(30)

submit_button.click()

print("Checking login status...")
time.sleep(3)


if "m-topbar__userpic" in driver.page_source:
    print("Login Successful!")
else:
    print("Failed to login or captcha stopped the request.")




