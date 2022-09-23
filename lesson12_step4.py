from os import link
from selenium import webdriver

import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link =  "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element_by_xpath('//*[@id="treasure"]')
    x = chest.get_attribute('valuex')
    y = calc(x)

    input = browser.find_element_by_xpath('//*[@id="answer"]')
    input.send_keys(y)

    checkbox1 = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    checkbox1.click()

    checkbox2 = browser.find_element_by_xpath('//*[@id="robotsRule"]')
    checkbox2.click()

    button = browser.find_element_by_xpath('/html/body/div/form/div/div/button')
    button.click()

    print(x)
    print(y)

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

