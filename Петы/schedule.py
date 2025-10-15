from typing import List

def create_schedule(pool: dict, *args: dict):
    for key, value in pool.items():
        #if key == 'набор':
        #    continue
        for i, item in enumerate(value):
            if item is None:
                continue
            for arg in args:
                if arg[key][i] is None and not(item[0] in arg['набор']):
                    if item[1] != 0:
                        item[1] -= 1
                        arg[key][i] = item[0]
                        arg['набор'].append(item[0])
    return args


pool = {
    'день1': [['адии-практика', 1], ['диск-лекция', 1], ['матан-практика', 1]],
    'день2': [['адии-практика', 1], ['диск-лекция', 1], None],
    'день3': [['матан-лекция', 2], ['матан-практика', 1], None],
    #'набор': ['адии-практика', 'диск-лекция', 'матан-лекция', 'матан-практика']
}

group_1 = {
    'день1': [None, None, None],
    'день2': [None, None, None],
    'день3': [None, None, None],
    'набор': []
}

group_2 = {
    'день1': [None, None, None],
    'день2': [None, None, None],
    'день3': [None, None, None],
    'набор': []
}

print(create_schedule(pool, group_1, group_2)[1])