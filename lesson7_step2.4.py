from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time, math

url = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(url)
 #   browser.implicitly_wait(5)

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), text_='100'))
    btn = browser.find_element_by_xpath('//*[@id="book"]')
    btn.click()

    x = browser.find_element_by_xpath('//*[@id="input_value"]').text
    y = calc(x)

    input_x = browser.find_element_by_xpath('//*[@id="answer"]')
    input_x.send_keys(y)

    button_sub = browser.find_element_by_xpath('/html/body/form/div/div/button')
    button_sub.click()

    alert = browser.switch_to.alert
    alert_text = (alert.text).split(': ')
    print("Код ДайВинчик: ", alert_text[1])




    

finally:
    time.sleep(5)
    browser.quit()