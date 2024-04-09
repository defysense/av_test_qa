import os
import requests
import sys
sys.path.append('../..')
import configuration as conf
from src.enums.global_enums import GlobalErrorMessages

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope='module')

def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def output_path_check():
    if not os.path.exists(conf.OUTPUT_DIR):
        os.makedirs(conf.OUTPUT_DIR)

def scroll_page(driver):
    driver.get(url=conf.SERVICE_URL)
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, conf.FULL_AREA)))
    ActionChains(driver).move_to_element(element).perform()

def make_screenshot(elements, test_num):
    values = {1: 'CO2', 3: 'water', 5: 'energy'}
    for i in range(1, 6, 2):
        element = elements[i]
        screenshot_file = os.path.join(conf.OUTPUT_DIR, f'test_{test_num}_element_{values[i]}.png')
        element.screenshot(screenshot_file)

# Визуальное отображение
def test_1_visual(driver):
    output_path_check()
    scroll_page(driver)
    element_full = driver.find_element(By.CSS_SELECTOR, conf.FULL_AREA)
    element_full.screenshot(os.path.join(conf.OUTPUT_DIR, 'test_1_element_full.png'))
    elements = driver.find_elements(By.CSS_SELECTOR, conf.ELEMENT_CSS_SELECTOR)
    make_screenshot(elements, 1)

# Отображение значений по умолчанию
def test_2_default_values(driver):
    output_path_check()
    scroll_page(driver)
    # elements = driver.find_elements(By.CSS_SELECTOR, conf.ELEMENT_CSS_SELECTOR)
    elements_value = driver.find_elements(By.CSS_SELECTOR, conf.VALUE_CSS_SELECTOR)
    make_screenshot(elements_value, 2)
    for element in elements_value:
        value = element.text.strip()
        assert value == "0", f"Expected default value, got {value}"

# Отображение числовых значений
def test_3_correct_values(driver):
    output_path_check()
    scroll_page(driver)
    # elements = driver.find_elements(By.CSS_SELECTOR, conf.ELEMENT_CSS_SELECTOR)
    elements_value = driver.find_elements(By.CSS_SELECTOR, conf.VALUE_CSS_SELECTOR)
    make_screenshot(elements_value, 3)
    # print(elements_value)

def test_4_correct_units(driver):


