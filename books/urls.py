from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.BooksListView.as_view(), name="books_list"),
    path("<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("create/", views.BookCreateView.as_view(), name="book_create"),
    path("<int:pk>/edit/", views.BookUpdateView.as_view(), name="book_update"),
    path("<int:pk>/delete/", views.book_delete_view, name="book_delete"),
]
