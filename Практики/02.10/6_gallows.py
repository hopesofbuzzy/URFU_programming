import os

"""
Виселица - игра для запуска в терминале, не в PyCharm
|----+
|    |
|    0
|  /-*-\
|    |
|   | |
|   | |
|
|____________
"""


def draw_gallow(stage: int):
    """
    Рисует виселицу на экране

    :param stage: стадия виселицы
    """
    draw("|----+\n|    |")

    draw("\n|    ")
    check_to_draw("0", stage, 1)

    draw("\n|  ")
    check_to_draw("/-", stage, 3)
    check_to_draw("*", stage, 2)
    check_to_draw("-\\", stage, 4)

    draw("\n|    ")
    check_to_draw("|", stage, 2)

    draw("\n|   ")
    check_to_draw("|", stage, 5)
    draw(" ")
    check_to_draw("|", stage, 6)

    draw("\n|   ")
    check_to_draw("|", stage, 5)
    draw(" ")
    check_to_draw("|", stage, 6)

    draw("\n|\n|____________")


def check_to_draw(char: str, stage: int, check: int):
    """
    Рисует элемент при условии stage >= check,
    иначе - заполняет элемент пустотой

    :param char: элемент для рисования
    :param stage: стадия виселицы
    :param check: необходимая для прорисовки элемента стадия виселицы
    """
    if stage >= check:
        print(char, end="")
    else:
        print(" " * len(char), end="")


def draw(char: str):
    """
    Рисует текст без перехода на новую строку

    :param char: элемент для рисования
    """
    print(char, end="")


word = "программирование"
guess = "".join(["_" for char in word])
stage = 0
attempts = []

while (stage <= 5) and (word != guess):
    os.system("cls")
    print("\n\nВИСЕЛИЦА\n")
    draw_gallow(stage)
    print(f"\n\nВы уже предлагали следующие буквы: {attempts}")
    print(f"\nОтгадываемое слово: {guess}")

    input_char = input("\nВведите букву: ")

    if len(input_char) != 1 or input_char in attempts:
        continue
    if input_char in word:
        guess = "".join(
            [
                guess[i] if char != input_char else input_char
                for i, char in enumerate(word)
            ]
        )
    else:
        stage += 1
    attempts += input_char

os.system("cls")
if word == guess:
    print("ВЫ ВЫИГРАЛИ!!!\n")
    print(f"Загаданным словом было: {word}\n\n^_^")
else:
    print("ВЫ ПРОИГРАЛИ\n")
    print(f"Загаданным словом было: {word}\n\n>_<")
input()
