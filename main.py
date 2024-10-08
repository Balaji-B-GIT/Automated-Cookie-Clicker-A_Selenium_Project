from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

URL = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)

cookie = driver.find_element(By.ID,value="cookie")
curser = int(driver.find_element(By.CSS_SELECTOR,value="#buyCursor b").text.split("-")[1].strip().replace(",",""))
grandma = int(driver.find_element(By.CSS_SELECTOR,value="#buyGrandma b").text.split("-")[1].strip().replace(",",""))
factory = int(driver.find_element(By.CSS_SELECTOR,value="#buyFactory b").text.split("-")[1].strip().replace(",",""))
mine = int(driver.find_element(By.CSS_SELECTOR,value="#buyMine b").text.split("-")[1].strip().replace(",",""))
shipment = int(driver.find_element(By.CSS_SELECTOR,value="#buyShipment b").text.split("-")[1].strip().replace(",",""))
lab = int(driver.find_element(By.ID,value="buyAlchemy lab").find_element(By.TAG_NAME,value="b").text.split("-")[1].strip().replace(",",""))
portal = int(driver.find_element(By.CSS_SELECTOR,value="#buyPortal b").text.split("-")[1].strip().replace(",",""))
time_mach = int(driver.find_element(By.ID,value="buyTime machine").find_element(By.TAG_NAME,value="b").text.split("-")[1].strip().replace(",",""))

timeout = time.time() + 5
five_min = time.time() + 60*5

def delayed_function():
    cookie_counter = int(driver.find_element(By.ID, value="money").text.replace(",",""))
    if cookie_counter >= time_mach:
        driver.find_element(By.ID,value="buyTime machine").click()
    elif cookie_counter >= portal:
        driver.find_element(By.ID, value="buyPortal").click()
    elif cookie_counter >= lab:
        driver.find_element(By.ID, value="buyAlchemy lab").click()
    elif cookie_counter >= shipment:
        driver.find_element(By.ID, value="buyShipment").click()
    elif cookie_counter >= mine:
        driver.find_element(By.ID, value="buyMine").click()
    elif cookie_counter >= factory:
        driver.find_element(By.ID, value="buyFactory").click()
    elif cookie_counter >= grandma:
        driver.find_element(By.ID, value="buyGrandma").click()
    elif cookie_counter >= curser:
        driver.find_element(By.ID, value="buyCursor").click()


while True:
    cookie.click()
    if time.time() > timeout:
        delayed_function()
        timeout = time.time() + 5
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break

