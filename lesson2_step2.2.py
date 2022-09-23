import select
from selenium import webdriver
from selenium.webdriver.support.select import Select

import time

link = 'http://suninjuly.github.io/selects1.html'

def calc(a, b):
    return (int(a) + int(b))
    
try:

    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element_by_xpath('//*[@id="num1"]').text
    b = browser.find_element_by_xpath('//*[@id="num2"]').text
    y = str(calc(a, b))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y) # ищем элемент с текстом "Python"

    button = browser.find_element_by_xpath('/html/body/div/form/button')
    button.click()


    #print('Начало', y, 'Конец')
    
finally:
    time.sleep(5)

    browser.quit()
