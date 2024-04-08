from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegLocators
from conftest import driver


class TestRegistration:
    def test_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register") # переход на страницу регистрации

        driver.find_element(*RegLocators.REGISTRATION_INPUT_NAME).send_keys("Светлана") # ввод имени
        driver.find_element(*RegLocators.INPUT_EMAIL).send_keys("ulyankinasveta7001@yandex.ru") #ввод почты
        driver.find_element(*RegLocators.INPUT_PASSWORD).send_keys("qwerty123") #ввод пароля
        driver.find_element(*RegLocators.REGISTRATION_BUTTON_REG).click() #клик на кнопке "Зарегистрироваться"

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegLocators.LOGIN_BUTTON))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login' # проверяем, что перешли на страницу "Вход" после регистрации

        driver.quit()
