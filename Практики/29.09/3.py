import random
import string

# Генерация пароля длины n из символов chars
def gen(chars, n):
    return ''.join([random.choice(chars) for i in range(n)])

password = gen(string.ascii_uppercase, 3) + gen(string.digits, 3) + gen('!@#$%^&*', 3)

print(password)
input()