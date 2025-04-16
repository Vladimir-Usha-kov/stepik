import math
import os
import time
import pytest
from selenium import webdriver
from selenium.types import WaitExcTypes
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import alert_is_present, new_window_is_opened
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')


def test_tesovich():
    try:
        link = 'https://suninjuly.github.io/file_input.html'
        driver.get(link)

        driver.find_element(By.NAME, 'firstname').send_keys('test')
        driver.find_element(By.NAME, 'lastname').send_keys('testovich')
        driver.find_element(By.NAME, 'email').send_keys('tes@test.ru')

        driver.find_element(By.ID, 'file').send_keys(file_path)
        driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
        time.sleep(3)
    finally:
        time.sleep(3)
        driver.quit()


def test_stepik():
    from selenium.webdriver.support.ui import Select
    import math
    def culc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    try:
        link = "https://suninjuly.github.io/redirect_accept.html"
        driver.get(link)

        driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()

        # confirm = driver.switch_to.alert
        # confirm.accept()
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)

        element_x = driver.find_element(By.ID, 'input_value').text

        result = culc(element_x)

        driver.find_element(By.ID, 'answer').send_keys(result)

        driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()

        driver.switch_to.window(driver.window_handles[0])
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        driver.quit()


def test_sel_lessons_wait():
    def culc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    try:
        driver.get('http://suninjuly.github.io/explicit_wait2.html')
        sale_button = WebDriverWait(driver, 12).until(
            (EC.text_to_be_present_in_element((By.ID, 'price'), '100')))
        driver.find_element(By.ID, 'book').click()

        element_x = driver.find_element(By.ID, 'input_value').text
        result = culc(element_x)
        driver.find_element(By.ID, 'answer').send_keys(result)

        driver.find_element(By.ID, 'solve').click()

    finally:
        time.sleep(5)
        driver.quit()
