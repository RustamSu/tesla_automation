from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import hlprs as hp
from faker import Faker
import random
import string
# import AllureReports
import unittest
import json
import time
import requests

fake = Faker()

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
# options.add_argument("--headless")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"C:\webdriver\chromedriver.exe")

# driver = webdriver.Chrome()
# driver.maximize_window()

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

driver.get(hp.job_search_url)
# time.sleep(2)
wait = WebDriverWait(driver, 3)

assert 'Careers | Tesla' in driver.title
print('Title is - ' + '"' + driver.title + '"')

# description
print('"' + driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute("content") + '"' + ' is in '
                                                                                                          'description')

assert (driver.find_element(By.XPATH, hp.search_name))
assert (driver.find_element(By.XPATH, hp.search_field))
try:
    wait.until((EC.visibility_of_element_located((By.XPATH, hp.search_field))))
except:
    print("Search field is invisible")

# random 3 letters
length = 3
letters = string.ascii_lowercase
rand_string = ''.join(random.choice(letters) for i in range(length))
# print("Random string of length", length, "is:", rand_string)
driver.find_element(By.XPATH, hp.search_field).send_keys(rand_string)

assert (driver.find_element(By.XPATH, hp.job_cat_nm))
driver.find_element(By.XPATH, hp.job_cat_field).click()
time.sleep(1)
driver.find_element(By.XPATH, hp.job_cat).click()

assert driver.find_element(By.XPATH, hp.region_name)
driver.find_element(By.XPATH, hp.region_field).click()
time.sleep(1)
driver.find_element(By.XPATH, hp.region).click()

assert driver.find_element(By.XPATH, hp.location_name)
driver.find_element(By.XPATH, hp.location_field).click()
time.sleep(1)
driver.find_element(By.XPATH, hp.location).click()

assert driver.find_element(By.XPATH, hp.state_name)
driver.find_element(By.XPATH, hp.state_field).click()
time.sleep(1)
driver.find_element(By.XPATH, hp.state).click()

assert driver.find_element(By.XPATH, hp.city_name)
driver.find_element(By.XPATH, hp.city_field).click()
time.sleep(1)
driver.find_element(By.XPATH, hp.city).click()

driver.find_element(By.XPATH, hp.reset_filters).click()

driver.find_element(By.XPATH, hp.search_field).send_keys("QA")

try:
    wait.until((EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(),'QA')]"))))
except:
    print('No result found')

menu = driver.find_elements(By.XPATH, "//tbody/tr")
map_menu = []
print(len(menu))
for x in menu:
    d = {}
    t = x.find_element(By.XPATH, './/td/a') # (//span[@class='_36FgXW0Q2msQwZW_DXRMDP'])
    n = t.get_attribute("text")
    l = t.get_attribute('href')
    r = requests.get(l)
    d['name'] = n
    d['link'] = l
    d['status code'] = r.status_code
    if r.status_code != 200:
        print(f'Fail!!! - {n}, {l}, Status Code is {r.status_code}')
    else:
        print(f'OK - {n}, {l}')
    map_menu.append(d)
with open('job_search_result.json', 'w') as json_file:
    json.dump(map_menu, open('job_search_result.json', 'w'))


'''menu = driver.find_elements_by_xpath('//tbody/tr')
for x in menu:
    r = x.find_element_by_xpath('.//td/a')
    l = r.get_attribute('href')
    print(r.text)
    print(l)
print(len(menu))'''



time.sleep(4)
driver.quit()
