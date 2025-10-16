import datetime


class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Класс Book для книги с информацией о ней

        :param title: название книги
        :param author: автор книги
        :param year: год издания
        """
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str:
        """
        Получает информацию о книге

        :return: информация о книге в строчном формате в виде <Автора> "<Название>" <год издания>
        """
        return f"{self.author} '{self.title}' {self.year} г. Возраст: {self.age}"

    def __str__(self):
        """
        Возвращает книгу в строчном формате

        :return: строчный вывод книги
        """
        return self.info()

    def __eq__(self, other):
        """
        Сравнивает объекты типа Book

        :return: результат сравнения
        """
        return isinstance(other, Book) and self.title == other.title

    @property
    def age(self):
        """
        Получает возраст книги

        :return: возраст книги
        """
        return datetime.datetime.now().year - self.year

    @age.setter
    def age(self, value):
        """
        Задает возраст книгу

        :param value: возраст книги для записи
        """
        self.year = datetime.datetime.now().year - value

    @classmethod
    def from_string(cls, data: str):
        """
        Класс для книги с информацией о ней
        :param data: данные о книге в формате <Автора>;<Название>;<год издания>
        """
        title, author, year = data.split(";")
        return cls(title, author, int(year))


book1 = Book("Преступление и наказание", "Достоевский", 2020)
print(book1.info())
print(book1)

book2 = Book.from_string("Война и мир;Толстой;2010")
print(book2.age)
book2.age = 50
print(book2.age)
print(book2)

book3 = Book.from_string("Война и мир;Толстой;2010")
print(book2 == book3)
