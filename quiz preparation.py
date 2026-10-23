from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
query = "laptop"
file = 0
for page in range(1, 5):
    driver.get(f"https://www.daraz.pk/catalog/?page={page}&q={query}&spm=a2a0e.tm80486640.search.d_go")
    elems= driver.find_elements(By.CLASS_NAME, "Bm3ON")
    print(f"{len(elems)} items found")

    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d) 
        file += 1
    # print(elem.text)
    # print(elem.get_attribute("outerHTML"))

    # time.sleep(4)
driver.close()
