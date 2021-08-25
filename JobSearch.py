from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, \
    ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import key, hlprs as hp
from faker import Faker
import requests
import unittest
import time
import json
import random
import string
import HtmlTestRunner

# import random

fake = Faker()


class Chrome(unittest.TestCase):  # Создаем класс теста, пишем всегда (unittest.TestCase)

    def setUp(self):
        desired_cap = {
            'browser': 'Chrome',
            'browser_version': 'latest',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1920x1080',
            'name': 'Bstack-[Python] Chrome Test'
        }
        url = key.mykey1
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)
        # self.driver = webdriver.Chrome()  #Присвоили драйверу значение Chrome (инициализатор)

    # Methods in UnitTest should start from "test" keyword
    def test_fullscreen(self):
        driver = self.driver  # Присвоили для этого метода driver = self.driver, чтобы обратилься к setUp
        driver.maximize_window()
        driver.get(hp.job_search_url)
        wait = WebDriverWait(driver, 3)

        # title
        assert 'Careers | Tesla' in driver.title
        print('Title is - ' + '"' + driver.title + '"')

        # description
        print('"' + driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute(
            "content") + '"' + ' is in description')

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

        driver.find_element(By.XPATH, hp.search_field).send_keys("Qa")

        menu = driver.find_elements(By.XPATH, "//tbody/tr")
        map_menu = []
        print(len(menu))
        for x in menu:
            d = {}
            t = x.find_element(By.XPATH, './/td/a')  # (//span[@class='_36FgXW0Q2msQwZW_DXRMDP'])
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
        with open('job_search_chrome1.json', 'w') as json_file:
            json.dump(map_menu, open('job_search_chrome1.json', 'w'))

    def tearDown(self):
        self.driver.quit()


class Chrome2(unittest.TestCase):  # Создаем класс теста, пишем всегда (unittest.TestCase)

    def setUp(self):
        desired_cap = {
            'browser': 'Chrome',
            'browser_version': '91.0',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1920x1080',
            'name': 'Bstack-[Python] Chrome Test'
        }
        url = key.mykey1
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)
        # self.driver = webdriver.Chrome()  #Присвоили драйверу значение Chrome (инициализатор)

        # Methods in UnitTest should start from "test" keyword

    def test_1150x750(self):
        driver = self.driver  # Присвоили для этого метода driver = self.driver, чтобы обратилься к setUp
        driver.set_window_size(1150, 750)
        driver.get(hp.job_search_url)
        wait = WebDriverWait(driver, 3)

        # title
        assert 'Careers | Tesla' in driver.title
        print('Title is - ' + '"' + driver.title + '"')

        # description
        print('"' + driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute(
            "content") + '"' + ' is in description')

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

        driver.find_element(By.XPATH, hp.search_field).send_keys("Qa")

        menu = driver.find_elements(By.XPATH, "//tbody/tr")
        map_menu = []
        print(len(menu))
        for x in menu:
            d = {}
            t = x.find_element(By.XPATH, './/td/a')  # (//span[@class='_36FgXW0Q2msQwZW_DXRMDP'])
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
        with open('job_search_chrome2.json', 'w') as json_file:
            json.dump(map_menu, open('job_search_chrome2.json', 'w'))

    def tearDown(self):
        self.driver.quit()


class Firefox(unittest.TestCase):  # 4.Second Unit test for Firefox browser

    def setUp(self):
        desired_cap = {
            'browser': 'firefox',
            'browser_version': 'latest',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1920x1080',
            'name': 'Bstack-[Python] Chrome Test'
        }
        url = key.mykey1
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)
        # self.driver = webdriver.Chrome()  #Присвоили драйверу значение Chrome (инициализатор)

        # Methods in UnitTest should start from "test" keyword

    def test_fullscreen(self):
        driver = self.driver  # Присвоили для этого метода driver = self.driver, чтобы обратилься к setUp
        driver.maximize_window()
        driver.get(hp.job_search_url)
        wait = WebDriverWait(driver, 3)

        # title
        assert 'Careers | Tesla' in driver.title
        print('Title is - ' + '"' + driver.title + '"')

        # description
        print('"' + driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute(
            "content") + '"' + ' is in description')

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
            t = x.find_element(By.XPATH, './/td/a')  # (//span[@class='_36FgXW0Q2msQwZW_DXRMDP'])
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
        with open('job_search_firefox1.json', 'w') as json_file:
            json.dump(map_menu, open('job_search_firefox1.json', 'w'))

    def tearDown(self):
        self.driver.quit()


class Firefox2(unittest.TestCase):  # 4.Second Unit test for Firefox browser

    def setUp(self):
        desired_cap = {
            'browser': 'firefox',
            'browser_version': 'latest',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1920x1080',
            'name': 'Bstack-[Python] Chrome Test'
        }
        url = key.mykey1
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)
        # self.driver = webdriver.Chrome()  #Присвоили драйверу значение Chrome (инициализатор)

        # Methods in UnitTest should start from "test" keyword

    def test_1150x750(self):
        driver = self.driver  # Присвоили для этого метода driver = self.driver, чтобы обратилься к setUp
        driver.set_window_size(1150, 750)
        driver.get(hp.job_search_url)
        wait = WebDriverWait(driver, 3)

        # title
        assert 'Careers | Tesla' in driver.title
        print('Title is - ' + '"' + driver.title + '"')

        # description
        print('"' + driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute(
            "content") + '"' + ' is in description')

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

        driver.find_element(By.XPATH, hp.search_field).send_keys("Qa")

        menu = driver.find_elements(By.XPATH, "//tbody/tr")
        map_menu = []
        print(len(menu))
        for x in menu:
            d = {}
            t = x.find_element(By.XPATH, './/td/a')  # (//span[@class='_36FgXW0Q2msQwZW_DXRMDP'])
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
        with open('job_search_firefox2.json', 'w') as json_file:
            json.dump(map_menu, open('job_search_firefox2.json', 'w'))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

