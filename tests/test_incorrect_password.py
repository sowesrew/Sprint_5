from locators import RegLocators
from conftest import driver


class TestIncorrectPassword:
    def test_incorrect_password(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register") # переход на страницу регистрации

        driver.find_element(*RegLocators.REGISTRATION_INPUT_NAME).send_keys("Светлана") # ввод имени
        driver.find_element(*RegLocators.INPUT_EMAIL).send_keys("ulyankinasveta7906@yandex.ru@yandex.ru") # ввод почты
        driver.find_element(*RegLocators.INPUT_PASSWORD).send_keys("qwer") # ввод пароля
        driver.find_element(*RegLocators.REGISTRATION_BUTTON_REG).click() # клик на кнопке "Зарегистрироваться"

        incorrect_pass = driver.find_element(*RegLocators.REGISTRATION_P_INCORRECT_PASS)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register' and incorrect_pass.text == 'Некорректный пароль' # сравниваем текущий адрес с тем адресом, который должен оставаться, проверяем, что отображается надпись "Некорректный пароль"

        driver.quit()
