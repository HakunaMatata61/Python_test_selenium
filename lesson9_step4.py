from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Input user firstname
    input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
    print(input1)
    input1.send_keys("Ivan")

    # Input user lastname
    input2 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
    print(input2)
    input2.send_keys("Petrov")

    # Input user email
    input3 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
    #input3 = browser.find_element(by='class name', value='form-control.city')
    print(input3)
    input3.send_keys("test@test.com")
    
    # Send request
    button = browser.find_element_by_xpath('/html/body/div/form/button')
    button.click()

    # Timeout 1 second    
    time.sleep(1)

    # Choose element with text
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # Test registration
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Timeout for test result of script
    time.sleep(10)
    # Close browser
    browser.quit()