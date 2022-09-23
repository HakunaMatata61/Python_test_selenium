from tkinter import Button
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    checkbox1 = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    checkbox1.click()

    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    
    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_xpath('//*[@id="answer"]')
    input.send_keys(y)

    button = browser.find_element_by_xpath('/html/body/div/form/button')
    button.click()
finally:
    # Timeout for test result of script
    time.sleep(10)
    # Close browser
    browser.quit()