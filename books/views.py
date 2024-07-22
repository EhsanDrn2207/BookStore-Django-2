from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from .forms import BookForm
from .models import Book


class BooksListView(generic.ListView):
    model = Book
    template_name = "books/books_list.html"
    context_object_name = "books"

# def books_list_view(request):
#     books = Book.objects.all()
#     return render(request, "books/books_list.html", context={'books': books})


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"

# def book_detail_view(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, "books/book_detail.html", context={'book': book})


class BookCreateView(generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_create.html"
    context_object_name = 'form'

# def book_create_view(request):
#     if request.method == "POST":
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("books_list")
#     else:
#         form = BookForm()
#     return render(request, "books/book_create.html", context={'form': form})
#

def book_update_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(None or request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books_list")
    else:
        form = BookForm(instance=book)
    return render(request, "books/book_update.html", context={"form": form, "book": book})


def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("books_list")
    return render(request, "books/book_delete.html", context={"book": book})
