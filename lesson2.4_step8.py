from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math 

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 
  
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector("button.btn")
        # ждем нужную цену в $100
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()
    
    btn = browser.find_element_by_id("solve")

    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element_by_id("answer")
    input.send_keys(y);

    btn.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
