from django.shortcuts import render

from .models import Book


def books_list_view(request):
    books = Book.objects.all()
    return render(request, "books/books_list.html", context={'books': books})
