from django.shortcuts import render

# Create your views here.
def post_list(request):
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