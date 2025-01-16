# utils/random_data.py

import random
import string


def generate_random_email():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12)) + "@test.com"


def generate_random_password():
    return ''.join(
        random.choices(string.ascii_letters + string.punctuation + string.ascii_uppercase + string.digits, k=19))


def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))
