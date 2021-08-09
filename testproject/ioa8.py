# # 3 Feladat: Összeadó

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html')
try:
    # operandusok és opreátor megkeresése:
    num1 = int(driver.find_element_by_id('num1').text)
    num2 = int(driver.find_element_by_id('num2').text)
    op = driver.find_element_by_id('op')

    # kalkuláció gomb megnyomása
    driver.find_element_by_id('submit').click()

    # eredmény számmá (int) alakítása
    result = int(driver.find_element_by_id('result').text)

    # ellenőrzés
    if op.text == '+':
        my_result = num1 + num2
        assert my_result == result
    elif op.text == '-':
        my_result = num1 - num2
        assert my_result == result
    elif op.text == '*':
        my_result = num1 * num2
        assert my_result == result
finally:
    driver.close()
