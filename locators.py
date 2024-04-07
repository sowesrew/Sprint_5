from selenium.webdriver.common.by import By


class RegLocators: # класс локаторов
    # инпуты
    REGISTRATION_INPUT_NAME = (By.XPATH, ".//label[text() = 'Имя']/../input") # поле для ввода имени на странице регистрации
    INPUT_EMAIL = (By.XPATH, ".//label[text() = 'Email']/../input") # поле для ввода почты
    INPUT_PASSWORD = (By.XPATH, ".//label[text() = 'Пароль']/../input") # поле для ввода пароля
    # кнопки
    REGISTRATION_BUTTON_REG = (By.XPATH, ".//button[text() = 'Зарегистрироваться']") # кнопка "Зарегистрироваться"
    LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[text() = 'Войти в аккаунт']") # кнопка "Войти в аккаунт"
    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти']") # кнопка "Войти" при вводе логина и пароля
    BUTTON_PLACE_ORDER = (By.XPATH, ".//button[text() = 'Оформить заказ']") # кнопка "Оформить заказ"
    BUTTON_PROFILE = (By.XPATH, ".//p[text() = 'Личный Кабинет']") # кнопка "Личный кабинет"
    BUTTON_LOGIN_REG = (By.XPATH, ".//a[text() = 'Войти']") # кнопка "Войти" на странице регистрации / восстановления пароля
    BUTTON_EXIT = (By.XPATH, ".//button[text() = 'Выход']") # кнопка "Выход"
    P_KONSTRUCTOR = (By.XPATH, ".//p[text() = 'Конструктор']") # ссылка "Конструктор"
    BUTTON_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # логотип
    # лейбл
    REGISTRATION_P_INCORRECT_PASS = (By.XPATH, ".//p[text() = 'Некорректный пароль']") # лейбл "Некорректный пароль"
    # переключатели в конструкторе
    SWITCH_KONSTRUCTOR_BUN = (By.XPATH, ".//span[text() = 'Булки']/..") # переключатель "Булки"
    SWITCH_KONSTRUCTOR_SAUSE = (By.XPATH, ".//span[text() = 'Соусы']/..") # переключатель "Соусы"
    SWITCH_KONSTRUCTOR_FILL = (By.XPATH, ".//span[text() = 'Начинки']/..") # переключатель "Начинки"
    # элементы в конструкторе
    ELEMENT_BUN = (By.XPATH, ".//h2[text() = 'Булки']") # заголовок "Булки"
    ELEMENT_SAUSE = (By.XPATH, ".//h2[text() = 'Соусы']")  # заголовок "Соусы"
    ELEMENT_FILL = (By.XPATH, ".//h2[text() = 'Начинки']")  # заголовок "Начинки"
