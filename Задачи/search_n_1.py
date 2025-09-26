

print("Расчёт разрядов...")

# numsposranks
# 1: 9 (1, 2, 3, 4, 5... 8, 9)
# 2: 189 (1, 2, 3... 10, 11, 12, 12... 98, 99)
# 3: 288 (...)
# 4: 38889 (...)
# (...)

numposranks = {
    1: 9,
}

for i in range(2, 1000):
    last_ranks_amount = (10**(i-1)-1)
    numposranks[i] = numposranks[i-1] + (10**(i)-1-last_ranks_amount)*i

n = int(input("Введите позицию n цифры: "))

# counting starts at 0, 1, 2...
def get_pos(pos: int):
    rank = 1
    min_pos = 1
    min_num = 1
    while pos>numposranks[rank]:
        rank += 1
        min_pos = numposranks[rank-1]+1
        min_num = 10**(rank-1)
    # rank:10111213, 3's  inrank_pos is 7
    inrank_pos = pos-min_pos
    # rank: 10, 11, 12..., 11's inrank_num_pos is 1
    inrank_num_pos = inrank_pos//rank
    # num: 125, 5's innum_pos is 2
    innum_pos = inrank_pos%rank
    num = str(min_num+inrank_num_pos)

    #return rank, num, innum_pos, inrank_pos
    return num[innum_pos]

print("На позиции n в ряде (12345678910111213...) находится цифра: ", get_pos(n))