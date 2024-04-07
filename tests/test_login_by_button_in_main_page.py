from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import RegLocators

driver = webdriver.Chrome() # подключение браузера
driver.get("https://stellarburgers.nomoreparties.site/") # переход на главную страницу

driver.find_element(*RegLocators.LOGIN_BUTTON_MAIN).click() # нажать на кнопку "Войти в аккаунт"
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegLocators.LOGIN_BUTTON)) # ждём пока загрузится кнопка "Войти"

driver.find_element(*RegLocators.INPUT_EMAIL).send_keys("ulyankinasveta7_131@yandex.ru") #ввод почты
driver.find_element(*RegLocators.INPUT_PASSWORD).send_keys("qwerty123") #ввод пароля
driver.find_element(*RegLocators.LOGIN_BUTTON).click() #клик на кнопке "Войти"

WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegLocators.BUTTON_PLACE_ORDER)) # ждём пока загрузится кнопка "Оформить заказ"

place_order = driver.find_element(*RegLocators.BUTTON_PLACE_ORDER) # задаём переменную для кнопки "Оформить заказ"
assert place_order.text == 'Оформить заказ' # проверяем, что после регистрации появляется кнопка "Оформить заказ"

driver.quit()