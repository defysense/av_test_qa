## Тест-кейсы для счётчиков эко-вклада (десктоп)

**Цель**: Проверить корректность отображения данных на счётчиках эко-вклада пользователя (вода, CO2, электроэнергия) в десктопной версии.  

**Тестируемая функциональность:**  
- Отображение числовых значений  
- Отображение единиц измерения  
- Форматирование больших чисел  
- Отображение значений по умолчанию (при отсутствии данных)  
- Визуальное отображение счётчиков (дизайн, шрифты, расположение)  

**Предварительные условия:**  
- Доступ к десктопной версии приложения  
- Наличие "эталонных" скриншотов с корректным отображением счётчиков  

#### Тест-кейсы
- **Отображение значений по умолчанию:**  
Проверить, что при отсутствии данных с бэкенда на счётчиках отображаются нулевые значения или текст-заполнитель (например, "-").  
- **Отображение числовых значений:**  
Проверить отображение различных числовых значений на счётчиках: целые числа, числа с плавающей точкой, большие числа (тысячи, миллионы).  
Убедиться, что числа отображаются без искажений и ошибок.  
- **Отображение единиц измерения:**  
Проверить, что для каждого счётчика отображается корректная единица измерения (литры/метры кубические для воды, кг/тонны для CO2, кВт⋅ч/МВт⋅ч для электроэнергии).  
Убедиться, что единицы измерения меняются в зависимости от величины значения (например, переход с литров на метры кубические при достижении 1000 литров).  
- **Форматирование больших чисел:**  
Проверить, что большие числа форматируются для удобства чтения (например, использование пробелов-разделителей или сокращений: 1 000 000, 1 млн).  
- **Визуальное отображение:**  
Сравнить скриншоты счётчиков с "эталонными" скриншотами.  
Убедиться, что дизайн, шрифты, расположение элементов соответствуют требованиям.  
- **Адаптивность:**  
Проверить отображение счётчиков при разных размерах окна браузера.  
Убедиться, что элементы не перекрываются и остаются читаемыми.  
- **Дополнительные тесты:**  
Проверить поведение счётчиков при обновлении данных с бэкенда.  

#### Ожидаемые результаты  
Все числовые значения, единицы измерения и визуальные элементы отображаются корректно, согласно требованиям и "эталонным" скриншотам.  
Счётчики адаптируются к разным размерам окна браузера.  

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
        screenshot_file = os.path.join(conf.OUTPUT_DIR, f'test_{test_num}_{values[i]}.png')
        element.screenshot(screenshot_file)

def make_screenshot_small(elements, test_num):
    values = {1: 'CO2', 2: 'water', 3: 'energy'}
    i = 1
    for element in elements:
        screenshot_file = os.path.join(conf.OUTPUT_DIR, f'test_{test_num}_{values[i]}.png')
        element.screenshot(screenshot_file)
        i=i+1

# # Визуальное отображение
# def test_1_visual(driver):
#     output_path_check()
#     scroll_page(driver)
#     element_full = driver.find_element(By.CSS_SELECTOR, conf.FULL_AREA)
#     element_full.screenshot(os.path.join(conf.OUTPUT_DIR, 'test_1_full.png'))
#     elements = driver.find_elements(By.CSS_SELECTOR, conf.ELEMENT_CSS_SELECTOR)
#     make_screenshot(elements, 1)

# # Отображение значений по умолчанию
# def test_2_default_values(driver):
#     output_path_check()
#     scroll_page(driver)
#     # elements = driver.find_elements(By.CSS_SELECTOR, conf.ELEMENT_CSS_SELECTOR)
#     elements_value = driver.find_elements(By.CSS_SELECTOR, conf.VALUE_CSS_SELECTOR)
#     make_screenshot_small(elements_value, 2)
#     for element in elements_value:
#         value = element.text.strip()
#         assert value == "0", f"Expected default value, got {value}"

# # Отображение числовых значений
# def test_3_correct_values(driver):
#     output_path_check()
#     scroll_page(driver)
#     # elements = driver.find_elements(By.CSS_SELECTOR, conf.ELEMENT_CSS_SELECTOR)
#     elements_value = driver.find_elements(By.CSS_SELECTOR, conf.VALUE_CSS_SELECTOR)
#     make_screenshot_small(elements_value, 3)
#     # print(elements_value)

# Отображение единиц измерения
def test_4_correct_units(driver):
    output_path_check()
    scroll_page(driver)
    units_value = driver.find_elements(By.CSS_SELECTOR, conf.UNITS_CSS_SELECTOR)
    make_screenshot_small(units_value, 4)

# Отображение подписей
def test_5_correct_label(driver):
    output_path_check()
    scroll_page(driver)
    label_value = driver.find_elements(By.CSS_SELECTOR, conf.LABEL_CSS_SELECTOR)
    make_screenshot_small(label_value, 5)
