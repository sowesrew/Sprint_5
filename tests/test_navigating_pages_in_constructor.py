from locators import RegLocators
import pytest
from conftest import driver


class TestNavigatingPages:
    @pytest.mark.parametrize(
        'switch_element,head_element,head',
        [
            [RegLocators.SWITCH_KONSTRUCTOR_SAUSE, RegLocators.ELEMENT_SAUSE, 'Соусы'],
            [RegLocators.SWITCH_KONSTRUCTOR_FILL, RegLocators.ELEMENT_FILL, 'Начинки'],
        ]
    )
    def test_navigating_bun(self, switch_element, head_element, head, driver):
        driver.get("https://stellarburgers.nomoreparties.site/") # переход на главную страницу (также это страница конструктор)
        driver.find_element(*switch_element).click() # клик по переключателю
        element = driver.find_element(*head_element) # назначаем на заголовок переключателя переменную
        assert element.text == head # проверяем, что нашли заголовок
        driver.quit()

    @pytest.mark.parametrize(
        'switch_element,head_element,head',
        [
            [RegLocators.SWITCH_KONSTRUCTOR_FILL, RegLocators.ELEMENT_FILL, 'Начинки'],
            [RegLocators.SWITCH_KONSTRUCTOR_BUN, RegLocators.ELEMENT_BUN, 'Булки']
        ]
    )
    def test_navigating_sause(self, switch_element, head_element, head, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")  # переход на главную страницу (также это страница конструктор)
        driver.find_element(*RegLocators.SWITCH_KONSTRUCTOR_SAUSE).click() # переход на вкладку "Соусы"
        driver.find_element(*switch_element).click()  # клик по переключателю
        element = driver.find_element(*head_element)  # назначаем на заголовок переключателя переменную
        assert element.text == head  # проверяем, что нашли заголовок
        driver.quit()

    @pytest.mark.parametrize(
        'switch_element,head_element,head',
        [
            [RegLocators.SWITCH_KONSTRUCTOR_SAUSE, RegLocators.ELEMENT_SAUSE, 'Соусы'],
            [RegLocators.SWITCH_KONSTRUCTOR_BUN, RegLocators.ELEMENT_BUN, 'Булки']
        ]
    )
    def test_navigating_fill(self, switch_element, head_element, head, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")  # переход на главную страницу (также это страница конструктор)
        driver.find_element(*RegLocators.SWITCH_KONSTRUCTOR_FILL).click()  # переход на вкладку "Начинки"
        driver.find_element(*switch_element).click()  # клик по переключателю
        element = driver.find_element(*head_element)  # назначаем на заголовок переключателя переменную
        assert element.text == head  # проверяем, что нашли заголовок
        driver.quit()