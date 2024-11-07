from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from .forms import BookForm, CommentForm
from .models import Book


class BooksListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = "books/books_list.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.all().order_by("created_datetime")
    
# def books_list_view(request):
#     books = Book.objects.all()
#     return render(request, "books/books_list.html", context={'books': books})


@login_required
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comments = book.comment.all()
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            new_comment = comment.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment = CommentForm()
    else:
        comment = CommentForm()
    return render(request, "books/book_detail.html", context={
        'book': book,
        'comments': book_comments,
        "comment_form": comment
    }
        )


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_create.html"
    context_object_name = 'form'

    def form_valid(self, form):
        try:
            obj = form.save(commit=False)
            obj.user = self.request.user
            return super().form_valid(form)
        except IntegrityError as e:
            form.add_error(None, "A database error occurred: {}".format(e))
            return self.form_invalid(form)

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


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_update.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user or self.request.user.username == 'admin'

# def book_update_view(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == "POST":
#         form = BookForm(None or request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect("books_list")
#     else:
#         form = BookForm(instance=book)
#     return render(request, "books/book_update.html", context={"form": form, "book": book})


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("books_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user or self.request.user.username == 'admin'

# def book_delete_view(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == "POST":
#         book.delete()
#         return redirect("books_list")
#     return render(request, "books/book_delete.html", context={"book": book})
