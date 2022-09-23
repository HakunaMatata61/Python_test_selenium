from msilib.schema import CheckBox
from selenium import webdriver

import time, math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_xpath('//*[@id="input_value"]').text
    y = calc(x)

    input = browser.find_element_by_xpath('//*[@id="answer"]')
    input.send_keys(y)

    CheckBox1 = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    CheckBox1.click()

    browser.execute_script("window.scrollBy(0, 100);")

    CheckBox2 = browser.find_element_by_xpath('//*[@id="robotsRule"]')
    CheckBox2.click()

    button = browser.find_element_by_xpath('/html/body/div/form/button')
    button.click()

finally:
    time.sleep(5)
    browser.quit()