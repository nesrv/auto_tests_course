from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# 
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

submit_button = browser.find_element(By.ID, 'book')
submit_button.click()


x = browser.find_element(By.ID, 'input_value').text
y = calc(int(x))
answer = browser.find_element(By.ID, 'answer')
answer.send_keys(y)

submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
submit_button.click()

time.sleep(15)