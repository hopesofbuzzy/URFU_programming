from typing import List


class StudentIOT:
    def __init__(self):
        self.schedule = {
            "день1": [None, None, None],
            "день2": [None, None, None],
            "день3": [None, None, None],
            "набор": [],
        }
        self.subjects = [
            "адии-практика",
            "диск-лекция",
            "матан-лекция",
            "матан-практика",
        ]


class IOT:
    def __init__(self, n: int):
        self.pool = {
            "день1": [["адии-практика", 1], ["диск-лекция", 1], ["матан-практика", 1]],
            "день2": [["адии-практика", 1], ["диск-лекция", 1], None],
            "день3": [["матан-лекция", 2], ["матан-практика", 1], None],
        }
        self.students = [StudentIOT()] * n

        for key, value in self.pool.items():
            print(
                f'{key}: {", ".join(
                [f"{subject[0]} (ост: {subject[1]})" if subject is not None else "-------" for subject in value]
            )}'
            )

    def form_schedule(self):
        for key, value in self.pool.items():
            for i, item in enumerate(value):
                if item is None:
                    continue
                for group in self.students:
                    if group[key][i] is None and not (item[0] in group["набор"]):
                        if item[1] != 0:
                            item[1] -= 1
                            group[key][i] = item[0]
                            group["набор"].append(item[0])


my_iot = IOT(3)
