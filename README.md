# Sprint_5
Данный проект тестирует UI интерфейс сайта: https://stellarburgers.nomoreparties.site/

Проект содержит в себе папку tests с файлами тестов, файл локаторов [locators.py](locators.py), файл фикстур [conftest.py](conftest.py), файл с авторизационными статическими данными [data.py](data.py), файл с генерацией авторизационных данных [helpers.py](heplpers.py) и [.gitignore](.gitignore)

Описание тестов из папки tests:
1. test_exit - выход из аккаунта
2. test_incorrect_password - тестирование на некорректный пароль при регистрации 
3. test_login_by_button_in_main_page - тестирование входа через кнопку "Войти в аккаунт" на главной
4. test_login_by_password_recovery - тестирование входа через кнопку в форме восстановления пароля
5. test_login_by_profile - тестирование входа через кнопку "Личный кабинет"
6. test_login_by_registration_form - тестирование через кнопку "Войти" в форме регистрации
7. test_navigating_pages_in_constructor - тестирование переключения вкладок в конструкторе
8. test_registration - тестирование регистрации на сайт
9. test_switch_by_profile - тестирование перехода на личный кабинет
10. test_switch_from_profile_to_constructor - тестирование перехода на конструктор через кнопку "Конструктор" и через логотип