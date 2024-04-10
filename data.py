import random
import string


class AuthorizationData:
    login = 'ulyankinasveta7_131@yandex.ru'
    password = 'qwerty123'

    @staticmethod
    def email_generator():
        email = str(random.choice(string.ascii_letters)) + str(random.randint(1, 999)) + '@ya.ru'
        return email