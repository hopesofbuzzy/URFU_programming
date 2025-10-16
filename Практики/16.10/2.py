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
        return f'{self.author} "{self.title}" {self.year} г.'


class EBook(Book):
    def __init__(self, title: str, author: str, year: int, format: str):
        """
        Наследуется от Book. Класс EBook для книги с форматом

        :param title: название книги
        :param author: автор книги
        :param year: год издания
        :param format: формат книги
        """
        super().__init__(title, author, year)
        self.format = format

    def info(self) -> str:
        """
        Метод наследуется от Book. Получает информацию о книге

        :return: информация о книге в строчном формате в виде <Автора> "<Название>" <год издания> <формат книги>
        """
        return f'{self.author} "{self.title}" {self.year} г. Формат: {self.format}'


my_ebook = EBook("Преступление и наказание", "Достоевский", 2020, "Электронная")
my_book  = Book("Преступление и наказание", "Достоевский", 2020)
print(my_book.info())
print(my_ebook.info())