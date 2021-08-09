## 4 Feladat: Email mező

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
driver.get('https://black-moss-0a0440e03.azurestaticapps.net/mm43.html')

# email cím kitöltése és kattintás a 'Submit Now!' gombra


def email_valid(email):
    email_field = driver.find_element_by_id('email')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'email')))

    email_field.clear()
    email_field.send_keys(email)

    driver.find_element_by_id('submit').click()


error_message = driver.find_element_by_xpath('//div[@class="validation-error"]')

if error_message:
# * Helyes kitöltés esete:
#     * email: teszt@elek.hu
#     * Nincs validációs hibazüzenet

email_valid('teszt@elek.hu')
error_message = driver.find_element_by_xpath('//div[@class="validation-error"]').is_displayed()
assert error_message.is_displayed()

# * Helytelen:
#     * email: teszt@
#     * Please enter a part following '@'. 'teszt@' is incomplete.

email_valid('teszt@')
helytelen_error_message = driver.find_element_by_xpath('//div[@class="validation-error"]').text
assert helytelen_error_message == 'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.'

# * Üres:
#     * email: <üres>
#     * b: <üres>
#     * Please fill out this field.

email_valid('')
ures_error_message = driver.find_element_by_xpath('//div[@class="validation-error"]').text
assert ures_error_message == 'Kérjük, töltse ki ezt a mezőt.'