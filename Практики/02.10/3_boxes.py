def print_back_report(count: int):
    """
    Выводит информацию о том, можно ли определённое
    количество пирожных расфосавать в коробки
    строго по 3 или строго по 4

    :param count: количество пирожных
    """
    if (count % 3 == 0) and (count % 5 == 0):
        print(f"{count} - расфасуем по 3 или по 5")
    elif count % 3 == 0:
        print(f"{count} - рафасуем по 3")
    elif count % 5 == 0:
        print(f"{count} - рафасуем по 5")
    else:
        print(f"{count} - не заказываем!")


print_back_report(int(input("Введите количество пироженых: ")))
