roman_digit_dictionary: dict = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}


def roman_to_digit(roman: str):
    """
    Получает римские цифры и переводит их в обычный формат

    :param roman: римские цифры в формате строки
    :return: обычное число
    """
    digit = 0
    while roman:
        digit += _read_roman(roman)[0]  # считываем первую римскую цифру
        roman = _read_roman(roman)[1]  # присваиваем отсавшуюся часть римского числа
    return digit


def digit_to_roman(digit: int):
    """
    Получает обычные числа и переводит их римские

    :param digit: обычное число
    :return: римские цифры
    """
    roman = ""
    while digit:
        roman += _read_digit(digit)[
            0
        ]  # вычитаем из обычного числа наиб. подходящую римскую цифру
        digit = _read_digit(digit)[1]  # присваиваем отсавшуюся часть обычного числа
    return roman


def _read_roman(roman: str):
    """
    Считывает в строке одну римскую цифра вида (I, II, III, IV, V...)
    и переводит её в обычный формат

    :param roman: строка с римскими цифрами
    :return: кортёж формата (
        одна полученная обычная цифра,
        оставшаяся непрочитанной часть строки с римскими цифрами
    )
    """
    chars = ""
    r = ()
    for i, char in enumerate(roman):
        chars += char
        if chars in roman_digit_dictionary:
            r = (roman_digit_dictionary[chars], roman[i + 1 :])
    return r


def _read_digit(digit: int):
    """
    Поэтапно считывает (вычитает) из обычного числа наибольшую римскую цифру вида (I, II, III, IV, V...)
    и переводит вычтенное в формат римской цифры (51-L=1, вычли 50 и вернули кортёж (L,1))

    :param roman: обычное число
    :return: кортёж формата (
        одна полученная римская цифра,
        оставшаяся часть обычного числа
    )
    """
    for key in sorted(
        roman_digit_dictionary, key=roman_digit_dictionary.get, reverse=True
    ):
        if digit >= roman_digit_dictionary[key]:
            return (key, digit - roman_digit_dictionary[key])


roman_tests = ["XXIII", "MMXXIII", "XLVI"]
digit_tests = [34, 543, 85, 2023]
print([roman_to_digit(roman) for roman in roman_tests])
print([digit_to_roman(digit) for digit in digit_tests])
