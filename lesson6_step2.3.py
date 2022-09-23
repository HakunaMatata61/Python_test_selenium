from selenium import webdriver

import time, math

link_1 = 'http://suninjuly.github.io/alert_accept.html'

link_2 = 'https://stepik.org/lesson/184253/step/4?unit=158843'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link_1)

    button = browser.find_element_by_xpath('/html/body/form/div/div/button')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_xpath('//*[@id="input_value"]').text
    y = calc(x)

    input_x = browser.find_element_by_xpath('//*[@id="answer"]')
    input_x.send_keys(y)

    button_submit = browser.find_element_by_xpath('/html/body/form/div/div/button')
    button_submit.click()

    alert = browser.switch_to.alert
    alert_text = (alert.text).split(': ')


    browser = webdriver.Chrome()
    browser.get(link_2)
    


    print('Кодовое слово', alert_text[1])


finally:
    time.sleep(15)
    browser.quit()