## 5 Feladat: Kakukktojás - városok

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://black-moss-0a0440e03.azurestaticapps.net/rv4.html')

try:
    time.sleep(5)


    cities = driver.find_element_by_id('cites')
    cities_list = str(cities.text).replace('"', ',').split(',')
    print(cities_list)
    random = []
    random_cities = driver.find_elements_by_xpath('//ul/li')

    for city in random_cities:
        if not city.text in cities_list:
            missing_city = city.text
        else:
            print(city.text, 'bennevan')



    driver.find_element_by_id('missingCity').send_keys(missing_city)

    driver.find_element_by_id('submit').click()
finally:
    driver.close()