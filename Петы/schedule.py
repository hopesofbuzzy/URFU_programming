from typing import List

def create_schedule(pool: dict, groups: List[dict]) -> List[dict]:
    ...

pool = {
    'день1': ['адии-практика', 'диск-лекция', 'матан-практика'],
    'день2': ['адии-практика', 'диск-лекция', None],
    'день3': ['матан-лекция' 'матан-практика', None],
}

group_1 = {
    'день1': [None, None, None],
    'день2': [None, None, None],
    'день3': [None, None, None],
}