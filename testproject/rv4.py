## 5 Feladat: Kakukktojás - városok

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from random import randint

driver = webdriver.Chrome()
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://black-moss-0a0440e03.azurestaticapps.net/rv4.html')

time.sleep(5)


cities = driver.find_element_by_id('cites')
cities_ = str(cities.text).replace('"', '')
cities_list = sorted(cities_.replace(',', '').split())

random = []
random_cities = driver.find_elements_by_xpath('//ul/li')
for city in random_cities:
    random.append(sorted(city.text))

