from django.shortcuts import render


# Create your views here.
def post_list(request):
    """
    Отображает список книг на странице

    :param request: запрос, на основе которого отображается список
    """
    # Заглушка данных для отображения
    books = [
        {
            'title': 'Война и мир',
            'author': 'Толстой',
            'content': 'Ура!',
        },
        {
            'title': 'Война и мир - 2',
            'author': 'Толстой-2',
            'content': 'Непрошенный сиквел',
        }
    ]

    return render(request, 'catalog/book_detail.html', {'books': books})