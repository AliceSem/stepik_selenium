from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link) 

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("alisa")

    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("super")

    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']") 
    input3.send_keys("alise@mail.ru")

    input4 = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    file_path = os.path.join(os.path.dirname(__file__), 'file_example.txt') # полный путь к файлу
    input4.send_keys(file_path)

     # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

