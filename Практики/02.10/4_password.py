import random
import string
import traceback


def generate_password(
    is_lower: bool, is_upper: bool, is_spec: bool, is_digit: bool, length: int
):
    """
    Генерирует пароль с параметрами

    :param is_lower: имеет никий регистр
    :param is_upper: имеет верхний регистр
    :param is_spec: имеет специальный символы
    :param is_digit: имеет числа
    :param length: длина пароля
    :return: сгенерированный пароль
    """
    chars_for_password = str()
    chars_for_password += (
        string.ascii_lowercase * is_lower + string.ascii_uppercase * is_upper
    )
    chars_for_password += "!@#$%" * is_spec + string.digits * is_digit
    return "".join([random.choice(chars_for_password) for i in range(length)])


def get_answer(text: str):
    """
    Получает вводные данные формата да/нет от пользователя

    :param text: текст интерфейса
    :return: True (да) False (нет)
    """
    answer = str(input(text)).lower()
    if not (answer in "да" or answer in "нет"):
        traceback.print_exc("Неверный тип данных!")
    return True if answer == "да" else False


print("Генерация пароля по параметрам.", end="\n\n")

has_lower = get_answer("Наличие нижнего регистра (да/нет): ")
has_upper = get_answer("Наличие верхнего регистра (да/нет): ")
has_spec = get_answer("Наличие спец. символов (да/нет): ")
has_digit = get_answer("Наличие чисел (да/нет): ")
length = int(input("Длина пароля (целое положит. число): "))
print("")

password = generate_password(has_lower, has_upper, has_spec, has_digit, length)
print(f"Сгенерированный пароль: {password}")
