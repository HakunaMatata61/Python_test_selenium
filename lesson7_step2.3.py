from selenium import webdriver

import time, math

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath('/html/body/form/div/div/button')
    button.click()
   # time.sleep(5)

    new_window = browser.window_handles

    browser.switch_to.window(new_window[0])
   # time.sleep(5)

    browser.switch_to.window(new_window[1])
   # time.sleep(5)

    x = browser.find_element_by_xpath('//*[@id="input_value"]').text
    y = calc(x)

    input_x = browser.find_element_by_xpath('//*[@id="answer"]')
    input_x.send_keys(y)

    button_sub = browser.find_element_by_xpath('/html/body/form/div/div/button')
    button_sub.click()

    alert = browser.switch_to.alert
    alert_text = (alert.text).split(': ')
    print("Код ДайВинчик: ", alert_text[1])
   # print('Окно 1', new_window[0], ' End', "Окно 2", new_window[1])

finally:
    time.sleep(5)
    browser.quit()