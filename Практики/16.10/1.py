class Book:
    def __init__(self, title: str, author: str, year):
        """
        Класс для книги с информацией о ней
        :param title: название книги
        :param author: автор книги
        :param year: год издания
        """
        self.title = title
        self.author = author
        self.year = int(year)

    def info(self) -> str:
        """
        Получает информацию о книге
        :return: информация о книге в строчном формате
        """
        return f'{self.author} "{self.title}" {self.year} г.'


my_book = Book("Преступление и наказание", "Достоевский", 2020)
print(my_book.info())
