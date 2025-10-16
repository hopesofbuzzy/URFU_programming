from abc import ABC, abstractmethod


class Printable(ABC):
    """
    Абстрактный класс Printable
    """

    @abstractmethod
    def print_info(self):
        """
        Абстрактный метод печатает информацию
        """
        pass


class Book(Printable):
    def __init__(self, title: str, author: str, year: int):
        """
        Наследуется от Printable. Класс Book для книги с информацией о ней

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
        return f'{self.author} "{self.title}" {self.year} г.'

    def print_info(self):
        """
        Метод наследуется от Printable. Печатает информацию о книге
        """
        print(self.info())


book1 = Book("Война и мир", "Толстой", 2020)
book1.print_info()
