# Задание: принимаем alert
# https://stepik.org/lesson/184253/step/4?unit=158843


import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = None

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()   
         
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(int(x))
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()
    
 
  

finally:
    time.sleep(10)
    if browser:
        browser.quit()