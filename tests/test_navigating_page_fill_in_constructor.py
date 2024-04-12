from locators import RegLocators
from conftest import driver


class TestNavigatingPages:

    def test_navigating_bun(self, driver):  # смотрим,что с переключателя "Булки" можем попасть на другие разделы
        driver.get("https://stellarburgers.nomoreparties.site/")  # переход на главную страницу (также это страница конструктор)
        driver.find_element(*RegLocators.SWITCH_KONSTRUCTOR_FILL).click()  # клик по переключателю
        element_fill = driver.find_element(*RegLocators.ELEMENT_FILL)  # назначаем на заголовок переключателя переменную
        assert element_fill.text == 'Начинки'  # проверяем, что нашли заголовок
