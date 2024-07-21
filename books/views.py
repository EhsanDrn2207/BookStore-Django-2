from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Book


def books_list_view(request):
    books = Book.objects.all()
    return render(request, "books/books_list.html", context={'books': books})


def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", context={'book': book})
