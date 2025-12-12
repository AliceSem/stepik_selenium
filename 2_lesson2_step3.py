from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def sum_values(x, y):
    return str(int(x) + int(y))

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text

    # Ваш код, который заполняет обязательные поля

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum_values(x, y))  # ищем элемент по тексту

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

   