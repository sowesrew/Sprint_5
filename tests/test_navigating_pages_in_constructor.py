from locators import RegLocators
from conftest import driver


class TestNavigatingPages:

    def test_navigating_bun(self, driver):  # проверяем переключатель "Булки"
        driver.get("https://stellarburgers.nomoreparties.site/")  # переход на главную страницу (также это страница конструктор)
        driver.find_element(*RegLocators.SWITCH_KONSTRUCTOR_FILL).click()  # клик по переключателю "Начинки"
        driver.find_element(*RegLocators.SWITCH_KONSTRUCTOR_BUN).click()  # клик по переключателю "Булки"
        element_bun = driver.find_element(*RegLocators.ELEMENT_BUN)  # назначаем на заголовок переключателя переменную
        assert element_bun.text == 'Булки'  # проверяем, что нашли заголовок

    def test_navigating_sause(self, driver):  # проверяем переключатель "Соусы"
        driver.get("https://stellarburgers.nomoreparties.site/")  # переход на главную страницу (также это страница конструктор)
        driver.find_element(*RegLocators.SWITCH_KONSTRUCTOR_SAUSE).click()  # клик по переключателю
        element_sause = driver.find_element(*RegLocators.ELEMENT_SAUSE)  # назначаем на заголовок переключателя переменную
        assert element_sause.text == 'Соусы' # проверяем, что нашли заголовок

    def test_navigating_fill(self, driver):  # проверяем переключатель "Начинки"
        driver.get("https://stellarburgers.nomoreparties.site/")  # переход на главную страницу (также это страница конструктор)
        driver.find_element(*RegLocators.SWITCH_KONSTRUCTOR_FILL).click()  # клик по переключателю
        element_fill = driver.find_element(*RegLocators.ELEMENT_FILL)  # назначаем на заголовок переключателя переменную
        assert element_fill.text == 'Начинки'  # проверяем, что нашли заголовок