from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.books_list_view, name="books_list"),
    path("<int:pk>/", views.book_detail_view, name="book_detail"),
    path("create/", views.book_create_view, name="book_create"),
]