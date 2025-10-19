SALARY = 10_000.0


class Employee:
    def __init__(self):
        """
        Класс для работника компании
        """
        self.salary_size = 0

    def calc_salary(self):
        return SALARY * self.salary_size


class Manager(Employee):
    def __init__(self):
        """
        Класс для менеджера
        """
        self.salary_size = 20


class Developer(Employee):
    def __init__(self):
        """
        Класс для разработчика
        """
        self.salary_size = 6


David = Developer()
Linda = Manager()
print(David.calc_salary())
print(Linda.calc_salary())
