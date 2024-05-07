from selenium.webdriver.common.by import By


class Locators:
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")  # Кнопка Личный кабинет
    CONSTRUCTOR_BUTTON = (By.XPATH, "//li/a[@href='/']")  # Кнопка Конструктор
    LOGIN_IN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка Войти в аккаунт
    AUTO_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа в аккаунт
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  # кнопка Востановить
    LOG_OUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка Выход
    REGISTRATION_LINK = (By.XPATH, "//a[@href ='/register']")  # Сыылка на регистрацию
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")  # Сылка входа в аккаунт
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")  # Ссылка на востановление пароля
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']//../input")  # Поле ввода Имя
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']//../input")  # Поле ввода Email
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Поле ввода пароля
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
    SAUCES_ITEM = (By.XPATH, "//span[text() = 'Соусы']/..")  # Вкладка Соусы
    BUN_ITEM = (By.XPATH, "//span[text() = 'Булки']/..")  # Вкладка Булки
    FILLING_ITEM = (By.XPATH, "//span[text() = 'Начинки']/..")  # Вкладка Начинки
    NOT_CORRECT_PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка ввода пароля
