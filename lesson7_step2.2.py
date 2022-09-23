from selenium import webdriver
from selenium.webdriver.common.by import By

import time, os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_fist_name = browser.find_element_by_xpath('/html/body/div/form/div/input[1]')
    input_fist_name.send_keys('Vasil')

    input_last_name = browser.find_element_by_xpath('/html/body/div/form/div/input[2]')
    input_last_name.send_keys('Ivanov')

    input_email = browser.find_element_by_xpath('/html/body/div/form/div/input[3]')
    input_email.send_keys('ivanov@test.com')

    current_dir = os.path.abspath(os.path.dirname('lesson7_step2.2.py'))
    file_name = 'qa.txt'
    file_path = os.path.join(current_dir, file_name)

   
    input_file = browser.find_element_by_xpath('//*[@id="file"]')
    input_file.send_keys(file_path)
    
    button = browser.find_element_by_xpath('/html/body/div/form/button')
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()