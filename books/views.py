from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from .forms import BookForm
from .models import Book


def books_list_view(request):
    books = Book.objects.all()
    return render(request, "books/books_list.html", context={'books': books})


def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", context={'book': book})


def book_create_view(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("books_list")
    else:
        form = BookForm()
    return render(request, "books/book_create.html", context={'form': form})