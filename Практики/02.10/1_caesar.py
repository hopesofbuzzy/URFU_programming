import string

# Получаем алфавиты русского и английского языков
rus = ''.join([chr(i) for i in range(ord('а'), ord('а')+32)])
eng = string.ascii_lowercase

def encrypt(text: str, shift: int):
    return _encryption(text, shift, 1)

def decrypt(text: str, shift: int):
    return _encryption(text, shift, -1)

def _encryption(text: str, shift: int, mode: int):
    '''
    Использует шифр Цезаря для расшифровки или зашифровки данных

    :param text: данные для зашифровки или расшифровки
    :param shift: сдвиг шифра
    :param mode: режим работы (1 = зашифровка, -1 = расшифровка)
    :return:
    '''
    alphabet = rus if text[0] in rus else eng
    decrypted_text = str()
    for char in text:
        decrypted_text += alphabet[(alphabet.index(char) + shift*mode) % len(alphabet)]
    return decrypted_text

text_to_encrypt = str(input("Введите слово для зашифровки: "))
shift_to_encrypt = int(input("Введите сдвиг (-5, 4, 0, 20) для шифра: "))
print(encrypt(text_to_encrypt, shift_to_encrypt), end='\n\n')

text_to_decrypt = str(input("Введите слово для расшифровки: "))
shift_to_decrypt = int(input("Введите сдвиг (-5, 4, 0, 20) для шифра: "))
print(decrypt(text_to_decrypt, shift_to_decrypt))