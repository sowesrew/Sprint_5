from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from locators import RegLocators
from conftest import driver
from data import AuthorizationData


class TestSwitchFromProfile:
    @pytest.mark.parametrize('button', [RegLocators.P_KONSTRUCTOR, RegLocators.BUTTON_LOGO])
    def test_switch(self, button, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login") # переход на страницу логина

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(RegLocators.LOGIN_BUTTON))  # ждём пока загрузится кнопка "Войти"
        driver.find_element(*RegLocators.INPUT_EMAIL).send_keys(AuthorizationData.login)  # ввод почты
        driver.find_element(*RegLocators.INPUT_PASSWORD).send_keys(AuthorizationData.password)  # ввод пароля
        driver.find_element(*RegLocators.LOGIN_BUTTON).click()  # клик на кнопке "Войти"

        driver.find_element(*RegLocators.BUTTON_PROFILE).click() # нажать на кнопку "Личный кабинет" уже залогиненным пользователем
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(RegLocators.BUTTON_EXIT)) # ждём пока загрузится кнопка "Выйти"
        driver.find_element(*button).click() # клик по кнопке "Конструктор" / логотип
        place_order = driver.find_element(*RegLocators.BUTTON_PLACE_ORDER) # задаём переменную для кнопки "Оформить заказ"
        assert place_order.text == 'Оформить заказ' # проверяем, что после регистрации появляется кнопка "Оформить заказ"
