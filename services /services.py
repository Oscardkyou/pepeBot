import random, string


# Генерация уникального реферального кода
def generate_referral_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))