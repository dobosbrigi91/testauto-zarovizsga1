# # 1. feladat

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://black-moss-0a0440e03.azurestaticapps.net/x234.html')

# függvény a téglalap kerületének kiszámolására:
def kerulet(a_oldal, b_oldal):

    # oldalak inputja:
    a = driver.find_element_by_id('a')
    b = driver.find_element_by_id('b')

    # mezők törlése
    a.clear()
    b.clear()

    # mezők kitöltése
    a.send_keys(a_oldal)
    b.send_keys(b_oldal)

    # kattintás a 'Kalkuláció' gombra
    driver.find_element_by_id('submit').click()
    return a, b


try:
    # várjon 10 mp-et, amíg betölt:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'a')))

    # * Helyes kitöltés esete:
    #     * a: 99
    #     * b: 12
    #     * Eredmény: 222

    kerulet(99, 12)
    result = driver.find_element_by_id('result')
    assert int(result.text) == 222

    # * Nem számokkal történő kitöltés:
    #     * a: kiskutya
    #     * b: 12
    #     * Eredmény: NaN

    kerulet('kiskutya', 12)
    assert result.text == 'NaN'

    # * Üres kitöltés:
    #     * a: <üres>
    #     * b: <üres>
    #     * Eredmény: NaN

    kerulet('', '')
    assert result.text == 'NaN'
finally:
    driver.close()
