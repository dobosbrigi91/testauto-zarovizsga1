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
cities_list = str(cities.text).replace('"', ',')
cities_list = cities_list.strip().split(',')
print(cities_list)
random = []
random_cities = driver.find_elements_by_xpath('//ul/li')

for city in random_cities:
    if not city.text in cities_list:
        print(city.text, 'hiányzik')
    else:
        print(city.text, 'bennevan')



#driver.find_element_by_id('missingCity').send_keys(missing_city)

#driver.find_element_by_id('submit').click()