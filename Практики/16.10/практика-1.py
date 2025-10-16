SALARY = 10_000.0


class Employee:
    def __init__(self):
        self.salary_size = 1

    def calc_salary(self):
        return SALARY * self.salary_size


class Manager(Employee):
    def __init__(self):
        self.salary_size = 2


class Developer(Employee):
    def __init__(self):
        self.salary_size = 1.5


David = Developer()
Linda = Manager()
print(David.calc_salary())
print(Linda.calc_salary())
