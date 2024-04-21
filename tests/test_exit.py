from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegLocators
from conftest import driver
from data import AuthorizationData


class TestExit:
    def test_exit(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")  # переход на страницу логина

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(RegLocators.LOGIN_BUTTON)) # ждём пока загрузится кнопка "Войти"
        driver.find_element(*RegLocators.INPUT_EMAIL).send_keys(AuthorizationData.login) # ввод почты
        driver.find_element(*RegLocators.INPUT_PASSWORD).send_keys(AuthorizationData.password) # ввод пароля
        driver.find_element(*RegLocators.LOGIN_BUTTON).click()  # клик на кнопке "Войти"

        driver.find_element(*RegLocators.BUTTON_PROFILE).click()  # нажать на кнопку "Личный кабинет" уже залогиненным пользователем

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(RegLocators.BUTTON_EXIT)) # ждём пока загрузится кнопка "Выход"
        driver.find_element(*RegLocators.BUTTON_EXIT).click()  # нажать на кнопку "Выход"

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(RegLocators.LOGIN_BUTTON)) # ждём пока загрузится кнопка "Вход"
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login' # после выхода проверяем, что оказываемся на странице логина
