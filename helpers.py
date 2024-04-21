import random
import string


class GenerationEmail:
    @staticmethod
    def email_generator():
        email = str(random.choice(string.ascii_letters)) + str(random.randint(1, 999)) + '@ya.ru'
        return email
