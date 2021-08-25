from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, ElementNotVisibleException
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
        driver.get(hp.tesla_url)
        wait = WebDriverWait(driver, 3)

        wait.until(EC.element_to_be_clickable((By.XPATH, hp.tesla_logo)))

        '''driver.get(hp.tesla_url)
        driver.maximize_window()
        time.sleep(2)'''

        driver.find_element(By.XPATH, hp.tesla_logo).click()  # click logo and renew page

        # title
        assert 'Electric Cars, Solar & Clean Energy | Tesla' in driver.title
        print(driver.title)

        # description
        print(driver.find_element(By.XPATH, "//head/meta[2]").get_attribute("content"))
        if driver.find_element(By.XPATH, "//head/meta[2]"):  # //meta[@name='description']
            print('I found the description')

        driver.find_element(By.XPATH, hp.Model_S).get_attribute("href")
        button = driver.find_element(By.XPATH, hp.Model_S)
        href_data = button.get_attribute('href')
        if href_data is None:
            is_clickable = False
        else:
            print(href_data)

        url_from_attr = driver.find_element(By.XPATH, hp.Model_S).get_attribute("href")
        url_from_attr_raw = "%r" % url_from_attr
        print(" URL from attribute -->> " + url_from_attr)
        print(" Raw string -->> " + url_from_attr_raw)

        menu = driver.find_elements_by_xpath(hp.side_menu)
        map_menu = []
        print(len(menu))
        for x in menu:
            d = {}
            t = x.get_attribute('textContent')
            l = x.get_attribute('href')
            r = requests.get(l)
            d['name'] = t
            d['link'] = l
            d['status code'] = r.status_code
            if r.status_code != 200:
                print(f'Fail!!! - {t}, {l}, Status Code is {r.status_code}')
            else:
                print(f'OK - {t}, {l}')
            map_menu.append(d)
        with open('output_chrome1.json', 'w') as json_file:
            json.dump(map_menu, open('output_chrome1.json', 'w'))

        # assertion header
        assert (driver.find_element(By.XPATH, hp.Model_3).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Model_X).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Model_Y).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Solar_Roof).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Solar_Panels).get_attribute("href"))
        assert (driver.find_element(By.XPATH,hp.Shop).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Account).get_attribute("href"))

        # driver.find_element(By.XPATH, "//span[contains(text(),'Menu')]").click()
        '''
        print(driver.find_element(By.XPATH, "//a[@href='/inventory/new/m3'][contains(.,'Existing Inventory')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/inventory/used/m3'][contains(.,'Used Inventory')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/tradein'][contains(.,'Trade-In')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/drive'][contains(.,'Test Drive')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/cybertruck'][contains(.,'Cybertruck')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/roadster'][contains(.,'Roadster')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/semi'][contains(.,'Semi')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/charging'][contains(.,'Charging')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/powerwall'][contains(.,'Powerwall')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/commercial'][contains(.,'Commercial Energy')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/utilities'][contains(.,'Utilities')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/findus'][contains(.,'Find Us')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/support'][contains(.,'Support')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='https://ir.tesla.com'][contains(.,'Investor Relations')]").get_attribute("href"))

        print(driver.find_element(By.XPATH, "//strong[contains(text(),'United States')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/teslaaccount'][contains(.,'Account')]").get_attribute("href"))'''

        # scrolling
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_S))
        driver.find_element(By.XPATH, hp.btn_Custom_Order).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Y))
        driver.find_element(By.XPATH, hp.btn_Existing_Inventory).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_3))
        driver.find_element(By.XPATH, hp.btn_Custom_Order).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_X))
        driver.find_element(By.XPATH, hp.btn_Existing_Inventory).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Solar_Panels))
        driver.find_element(By.XPATH, hp.btn_Order_Now).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Solar_Roof))
        driver.find_element(By.XPATH, hp.btn_Learn_More).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Accessories))
        driver.find_element(By.XPATH, hp.btn_Shop_Now).send_keys(Keys.PAGE_DOWN)

        # assertion footer menu
        assert (driver.find_element(By.XPATH, hp.About).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Legal).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Contact).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Career).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.News).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Engage).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Locations).get_attribute("href"))


    def tearDown(self):
        self.driver.quit()

class Chrome2(unittest.TestCase):  # Создаем класс теста, пишем всегда (unittest.TestCase)

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

    def test_1150x750(self):
        driver = self.driver  # Присвоили для этого метода driver = self.driver, чтобы обратилься к setUp
        driver.set_window_size(1150, 750)
        driver.get(hp.tesla_url)
        wait = WebDriverWait(driver, 3)

        wait.until(EC.element_to_be_clickable((By.XPATH, hp.tesla_logo)))

        '''driver.get(hp.tesla_url)
        driver.maximize_window()
        time.sleep(2)'''

        driver.find_element(By.XPATH, hp.tesla_logo).click()  # click logo and renew page

        # title
        assert 'Electric Cars, Solar & Clean Energy | Tesla' in driver.title
        print(driver.title)

        # description
        print(driver.find_element(By.XPATH, "//head/meta[2]").get_attribute("content"))
        if driver.find_element(By.XPATH, "//head/meta[2]"):  # //meta[@name='description']
            print('I found the description')

        driver.find_element(By.XPATH, hp.Model_S).get_attribute("href")
        button = driver.find_element(By.XPATH, hp.Model_S)
        href_data = button.get_attribute('href')
        if href_data is None:
            is_clickable = False
        else:
            print(href_data)

        url_from_attr = driver.find_element(By.XPATH, hp.Model_S).get_attribute("href")
        url_from_attr_raw = "%r" % url_from_attr
        print(" URL from attribute -->> " + url_from_attr)
        print(" Raw string -->> " + url_from_attr_raw)

        menu = driver.find_elements_by_xpath(hp.side_menu)
        map_menu = []
        print(len(menu))
        for x in menu:
            d = {}
            t = x.get_attribute('textContent')
            l = x.get_attribute('href')
            r = requests.get(l)
            d['name'] = t
            d['link'] = l
            d['status code'] = r.status_code
            if r.status_code != 200:
                print(f'Fail!!! - {t}, {l}, Status Code is {r.status_code}')
            else:
                print(f'OK - {t}, {l}')
            map_menu.append(d)
        with open('output_chrome2.json', 'w') as json_file:
            json.dump(map_menu, open('output_chrome2.json', 'w'))

        # assertion header
        assert (driver.find_element(By.XPATH, hp.Model_3).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Model_X).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Model_Y).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Solar_Roof).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Solar_Panels).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Shop).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Account).get_attribute("href"))

        # driver.find_element(By.XPATH, "//span[contains(text(),'Menu')]").click()
        '''
        print(driver.find_element(By.XPATH, "//a[@href='/inventory/new/m3'][contains(.,'Existing Inventory')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/inventory/used/m3'][contains(.,'Used Inventory')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/tradein'][contains(.,'Trade-In')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/drive'][contains(.,'Test Drive')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/cybertruck'][contains(.,'Cybertruck')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/roadster'][contains(.,'Roadster')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/semi'][contains(.,'Semi')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/charging'][contains(.,'Charging')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/powerwall'][contains(.,'Powerwall')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/commercial'][contains(.,'Commercial Energy')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/utilities'][contains(.,'Utilities')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/findus'][contains(.,'Find Us')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/support'][contains(.,'Support')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='https://ir.tesla.com'][contains(.,'Investor Relations')]").get_attribute("href"))

        print(driver.find_element(By.XPATH, "//strong[contains(text(),'United States')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/teslaaccount'][contains(.,'Account')]").get_attribute("href"))'''

        # scrolling
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_S))
        driver.find_element(By.XPATH, hp.btn_Custom_Order).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Y))
        driver.find_element(By.XPATH, hp.btn_Existing_Inventory).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_3))
        driver.find_element(By.XPATH, hp.btn_Custom_Order).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_X))
        driver.find_element(By.XPATH, hp.btn_Existing_Inventory).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Solar_Panels))
        driver.find_element(By.XPATH, hp.btn_Order_Now).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Solar_Roof))
        driver.find_element(By.XPATH, hp.btn_Learn_More).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Accessories))
        driver.find_element(By.XPATH, hp.btn_Shop_Now).send_keys(Keys.PAGE_DOWN)

        # assertion footer menu
        assert (driver.find_element(By.XPATH, hp.About).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Legal).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Contact).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Career).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.News).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Engage).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Locations).get_attribute("href"))

    def tearDown(self):
        self.driver.quit()

class Firefox(unittest.TestCase): # 4.Second Unit test for Firefox browser

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
        driver.get(hp.tesla_url)
        wait = WebDriverWait(driver, 3)

        wait.until(EC.element_to_be_clickable((By.XPATH, hp.tesla_logo)))

        '''driver.get(hp.tesla_url)
        driver.maximize_window()
        time.sleep(2)'''

        driver.find_element(By.XPATH, hp.tesla_logo).click()  # click logo and renew page

        # title
        assert 'Electric Cars, Solar & Clean Energy | Tesla' in driver.title
        print(driver.title)

        # description
        print(driver.find_element(By.XPATH, "//head/meta[2]").get_attribute("content"))
        if driver.find_element(By.XPATH, "//head/meta[2]"):  # //meta[@name='description']
            print('I found the description')

        driver.find_element(By.XPATH, hp.Model_S).get_attribute("href")
        button = driver.find_element(By.XPATH, hp.Model_S)
        href_data = button.get_attribute('href')
        if href_data is None:
            is_clickable = False
        else:
            print(href_data)

        url_from_attr = driver.find_element(By.XPATH, hp.Model_S).get_attribute("href")
        url_from_attr_raw = "%r" % url_from_attr
        print(" URL from attribute -->> " + url_from_attr)
        print(" Raw string -->> " + url_from_attr_raw)

        menu = driver.find_elements_by_xpath(hp.side_menu)
        map_menu = []
        print(len(menu))
        for x in menu:
            d = {}
            t = x.get_attribute('textContent')
            l = x.get_attribute('href')
            r = requests.get(l)
            d['name'] = t
            d['link'] = l
            d['status code'] = r.status_code
            if r.status_code != 200:
                print(f'Fail!!! - {t}, {l}, Status Code is {r.status_code}')
            else:
                print(f'OK - {t}, {l}')
            map_menu.append(d)
        with open('output_firefox1.json', 'w') as json_file:
            json.dump(map_menu, open('output_firefox1.json', 'w'))

        # assertion header
        assert (driver.find_element(By.XPATH, hp.Model_3).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Model_X).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Model_Y).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Solar_Roof).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Solar_Panels).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Shop).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Account).get_attribute("href"))

        # driver.find_element(By.XPATH, "//span[contains(text(),'Menu')]").click()
        '''
        print(driver.find_element(By.XPATH, "//a[@href='/inventory/new/m3'][contains(.,'Existing Inventory')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/inventory/used/m3'][contains(.,'Used Inventory')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/tradein'][contains(.,'Trade-In')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/drive'][contains(.,'Test Drive')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/cybertruck'][contains(.,'Cybertruck')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/roadster'][contains(.,'Roadster')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/semi'][contains(.,'Semi')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/charging'][contains(.,'Charging')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/powerwall'][contains(.,'Powerwall')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/commercial'][contains(.,'Commercial Energy')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/utilities'][contains(.,'Utilities')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/findus'][contains(.,'Find Us')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/support'][contains(.,'Support')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='https://ir.tesla.com'][contains(.,'Investor Relations')]").get_attribute("href"))

        print(driver.find_element(By.XPATH, "//strong[contains(text(),'United States')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/teslaaccount'][contains(.,'Account')]").get_attribute("href"))'''

        # scrolling
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_S))
        driver.find_element(By.XPATH, hp.btn_Custom_Order).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Y))
        driver.find_element(By.XPATH, hp.btn_Existing_Inventory).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_3))
        driver.find_element(By.XPATH, hp.btn_Custom_Order).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_X))
        driver.find_element(By.XPATH, hp.btn_Existing_Inventory).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Solar_Panels))
        driver.find_element(By.XPATH, hp.btn_Order_Now).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Solar_Roof))
        driver.find_element(By.XPATH, hp.btn_Learn_More).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Accessories))
        driver.find_element(By.XPATH, hp.btn_Shop_Now).send_keys(Keys.PAGE_DOWN)

        # assertion footer menu
        assert (driver.find_element(By.XPATH, hp.About).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Legal).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Contact).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Career).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.News).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Engage).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Locations).get_attribute("href"))

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
        driver.get(hp.tesla_url)
        wait = WebDriverWait(driver, 3)

        wait.until(EC.element_to_be_clickable((By.XPATH, hp.tesla_logo)))

        '''driver.get(hp.tesla_url)
        driver.maximize_window()
        time.sleep(2)'''

        driver.find_element(By.XPATH, hp.tesla_logo).click()  # click logo and renew page

        # title
        assert 'Electric Cars, Solar & Clean Energy | Tesla' in driver.title
        print(driver.title)

        # description
        print(driver.find_element(By.XPATH, "//head/meta[2]").get_attribute("content"))
        if driver.find_element(By.XPATH, "//head/meta[2]"):  # //meta[@name='description']
            print('I found the description')

        driver.find_element(By.XPATH, hp.Model_S).get_attribute("href")
        button = driver.find_element(By.XPATH, hp.Model_S)
        href_data = button.get_attribute('href')
        if href_data is None:
            is_clickable = False
        else:
            print(href_data)

        url_from_attr = driver.find_element(By.XPATH, hp.Model_S).get_attribute("href")
        url_from_attr_raw = "%r" % url_from_attr
        print(" URL from attribute -->> " + url_from_attr)
        print(" Raw string -->> " + url_from_attr_raw)

        menu = driver.find_elements_by_xpath(hp.side_menu)
        map_menu = []
        print(len(menu))
        for x in menu:
            d = {}
            t = x.get_attribute('textContent')
            l = x.get_attribute('href')
            r = requests.get(l)
            d['name'] = t
            d['link'] = l
            d['status code'] = r.status_code
            if r.status_code != 200:
                print(f'Fail!!! - {t}, {l}, Status Code is {r.status_code}')
            else:
                print(f'OK - {t}, {l}')
            map_menu.append(d)
        with open('output_firefox1.json', 'w') as json_file:
            json.dump(map_menu, open('output_firefox1.json', 'w'))

        # assertion header
        assert (driver.find_element(By.XPATH, hp.Model_3).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Model_X).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Model_Y).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Solar_Roof).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Solar_Panels).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Shop).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Account).get_attribute("href"))

        # driver.find_element(By.XPATH, "//span[contains(text(),'Menu')]").click()
        '''
        print(driver.find_element(By.XPATH, "//a[@href='/inventory/new/m3'][contains(.,'Existing Inventory')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/inventory/used/m3'][contains(.,'Used Inventory')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/tradein'][contains(.,'Trade-In')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/drive'][contains(.,'Test Drive')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/cybertruck'][contains(.,'Cybertruck')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/roadster'][contains(.,'Roadster')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/semi'][contains(.,'Semi')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/charging'][contains(.,'Charging')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/powerwall'][contains(.,'Powerwall')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/commercial'][contains(.,'Commercial Energy')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/utilities'][contains(.,'Utilities')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/findus'][contains(.,'Find Us')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/support'][contains(.,'Support')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='https://ir.tesla.com'][contains(.,'Investor Relations')]").get_attribute("href"))

        print(driver.find_element(By.XPATH, "//strong[contains(text(),'United States')]").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//a[@href='/teslaaccount'][contains(.,'Account')]").get_attribute("href"))'''

        # scrolling
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_S))
        driver.find_element(By.XPATH, hp.btn_Custom_Order).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Y))
        driver.find_element(By.XPATH, hp.btn_Existing_Inventory).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_3))
        driver.find_element(By.XPATH, hp.btn_Custom_Order).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_X))
        driver.find_element(By.XPATH, hp.btn_Existing_Inventory).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Solar_Panels))
        driver.find_element(By.XPATH, hp.btn_Order_Now).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Solar_Roof))
        driver.find_element(By.XPATH, hp.btn_Learn_More).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert (driver.find_element(By.XPATH, hp.logo_Accessories))
        driver.find_element(By.XPATH, hp.btn_Shop_Now).send_keys(Keys.PAGE_DOWN)

        # assertion footer menu
        assert (driver.find_element(By.XPATH, hp.About).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Legal).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Contact).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Career).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.News).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Engage).get_attribute("href"))
        assert (driver.find_element(By.XPATH, hp.Locations).get_attribute("href"))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))