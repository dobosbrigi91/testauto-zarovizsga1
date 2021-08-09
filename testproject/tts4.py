# # 2 Feladat: Pénzfeldobás

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://black-moss-0a0440e03.azurestaticapps.net/tts4.html')

try:
    # kattintás 100-szor a 'Pénzfeldobás' gombra
    for click in range(100):
        driver.find_element_by_id('submit').click()

    # eredmények listába gyűjtése:
    results = driver.find_elements_by_xpath('//ul/li')

    # fej találatok kigyűjtése
    fej = []
    for result in results:
        if result.text == 'fej':
            fej.append(result)

    assert len(fej) >= 30
finally:
    driver.close()
