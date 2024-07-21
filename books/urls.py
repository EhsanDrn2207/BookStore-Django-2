from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.books_list_view, name="books_list"),
]
