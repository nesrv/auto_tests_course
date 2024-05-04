# Задание: переход на новую вкладку
# https://stepik.org/lesson/184253/step/6?unit=158843


import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = None

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    # button = browser.find_element(By.CSS_SELECTOR, "button") # или
    # button = browser.find_element('xpath', '//button[@type="submit"]').click() # или
    submit_button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(int(x))
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    
    # browser.find_element('xpath', '//input[@class="form-control"]').send_keys(res)
    # browser.find_element('xpath', '//button[@type="submit"]').click()   

    time.sleep(2)

    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()
    
    alert = browser.switch_to.alert 
    
    # print(browser.switch_to.alert.text.split()[-1])
    print(alert.text)
    
    
    
 
  

finally:
    time.sleep(10)
    if browser:
        browser.quit()