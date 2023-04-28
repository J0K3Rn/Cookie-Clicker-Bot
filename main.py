from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_driver_path = "/Users/Joseph.Richardson@ibm.com/Documents/chromedriver/chromedriver"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #executable_path=chrome_driver_path)

# Open up website
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Let game load
time.sleep(5)

# Need to first select a language before starting
language_select = driver.find_element(By.ID, "langSelect-EN")
language_select.click()

# Let game load
time.sleep(5)

# Cookie object
cookie = driver.find_element(By.ID, "bigCookie")

# 5 minutes
five_min = time.time() + 60 * 5

while True:
    cookie.click()
    upgrades = driver.find_elements(By.CSS_SELECTOR, "div[class*='crate upgrade enabled']")
    if len(upgrades) >= 1:
        upgrades[-1].click()
    products = driver.find_elements(By.CSS_SELECTOR, "div[class*='product unlocked enabled']")
    if len(products) >= 1:
        products[-1].click()

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break

driver.quit()
