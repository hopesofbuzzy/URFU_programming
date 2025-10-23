import datetime
from decimal import Decimal
import re

DATE_FORMAT = "%Y-%m,%d"
goods: dict = {}


def add(items, title, amount, expiration_date=None):
    """
    Добавляет предметы в холодильник

    :param items: словарь с предметами холодильника
    :param title: название добавляемого предмета
    :param amount: количество добавляемого предмета
    :param expiration_date: срок годности добавляемого предмета
    :return: None
    """
    if expiration_date:
        expiration_date = datetime.datetime.strptime(
            expiration_date, r"%Y-%m-%d"
        ).date()
    items[title] = items.setdefault(title, [])
    items[title].append(
        {"amount": Decimal(str(amount)), "expiration_date": expiration_date}
    )


def add_by_note(items, note):
    """
    Добавляет в холодильник предметы в строчном формате

    :param items: словарь с предметами холодильника
    :param note: строка в формате <название предмета> <количество> <срок годности>
    :return: None
    """
    amount = expiration_date = title = None
    if re.match("[0-9]+-[0-9]+-[0-9]+", note.split()[-1]):
        amount, expiration_date = note.split()[-2:]
        title = " ".join(note.split()[:-2])

    else:
        amount = note.split()[-1]
        title = " ".join(note.split()[:-1])

    add(items, title, amount, expiration_date)


def find(items, needle):
    """
    Ищет продукты в холодильнкие по ключевому слову

    :param items: словарь с предметами холодильника
    :param needle: ключевое слово для поиска
    :return: список найденных продуктов
    """
    found = []
    for key in items.keys():
        if needle.lower() in key.lower():
            found.append(key)
    return found


def amount(items, needle):
    """
    Возвращает количество продукта в холодильнике. Считает количество во всех партиях

    :param items: словарь с предметами холодильника
    :param needle: строка для поиска продутка (без регистра)
    :return: количество продукта
    """
    amountt = Decimal("0")
    for key, value in items.items():
        if needle.lower() in key.lower():
            amountt += sum([part["amount"] for part in items[key]])
    return Decimal(str(amountt))

add(goods, "Молоко", 1, "2025-10-12")
add_by_note(goods, "Молоко 1 2025-10-13")
add_by_note(goods, "Молоко 1")
add_by_note(goods, "Яйца куриные 10 2025-09-29")
add_by_note(goods, "Яйца гусиные 10")

print(find(goods, "йц"))
print(amount(goods, "яйца куриные"))
print(goods)