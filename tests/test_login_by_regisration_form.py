from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegLocators
from conftest import driver
from data import AuthorizationData


class TestLoginFromRegistrationForm:
    def test_login_from_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register") # переход на страницу регистрации

        driver.find_element(*RegLocators.BUTTON_LOGIN_REG).click() #клик на кнопке "Войти" на странице регистрации
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegLocators.LOGIN_BUTTON))# ждём пока загрузится кнопка "Войти"

        driver.find_element(*RegLocators.INPUT_EMAIL).send_keys(AuthorizationData.login) #ввод почты
        driver.find_element(*RegLocators.INPUT_PASSWORD).send_keys(AuthorizationData.password) #ввод пароля
        driver.find_element(*RegLocators.LOGIN_BUTTON).click() #клик на кнопке "Войти"

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegLocators.BUTTON_PLACE_ORDER)) # ждём пока загрузится кнопка "Оформить заказ"

        place_order = driver.find_element(*RegLocators.BUTTON_PLACE_ORDER) # задаём переменную для кнопки "Оформить заказ"
        assert place_order.text == 'Оформить заказ' # проверяем, что после авторизации появляется кнопка "Оформить заказ"
