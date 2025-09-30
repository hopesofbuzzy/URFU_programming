import random
money = 1000

while money > 0:
    print(f"Ваш счёт: {money}")
    stavka = int(input("Введите вашу ставку: "))

    r = round(random.random(), 2)
    diff = round(abs(r - 0.5), 2)
    win = r > 0.5

    if win:
        money += stavka
        print(f"Вы выиграли с отрывом {diff} (Кубик: {r})")
        print(f"Вы получаете {stavka}")
    else:
        money -= stavka
        print(f"Вы проиграли с отрывом {diff} (Кубик: {r})")
        print(f"Вы лишились {stavka}")

    print('')

print(f"Вы проиграли со счётом {money}")