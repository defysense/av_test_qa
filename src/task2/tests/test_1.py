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

def test_screenshot(driver):
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    driver.get(url=conf.SERVICE_URL)
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, conf.FULL_AREA)))
    
    ActionChains(driver).move_to_element(element).perform()
    elements = driver.find_elements(By.CSS_SELECTOR, conf.ELEMENT_CSS_SELECTOR)
    for i in range(1, 6, 2):
        element = elements[i]
        screenshot_file = os.path.join(output_dir, f'element_{i}.png')
        element.screenshot(screenshot_file)
    
    
    
    # element_full = driver.find_element(By.CSS_SELECTOR, '.desktop-impact-items-F7T6E')
    # screenshot_file = os.path.join(output_dir, 'screenshot.png')
    # element_full.screenshot(os.path.join(output_dir, 'element_full_screenshot.png'))
    # element_co2.screenshot(os.path.join(output_dir, 'element_co2_screenshot.png'))
    # driver.save_screenshot(screenshot_file)


    # def test_getting_card():
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36', 'Accept': 'application/json'}
#     response = requests.get(url=SERVICE_URL, headers=headers)
#     # print(response.json())
#     assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value