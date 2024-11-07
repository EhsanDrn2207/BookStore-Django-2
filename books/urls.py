from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import BookViewSet, CommentViewSet, PublisherViewSet, CategoryViewSet 
from . import views


router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("", views.BooksListView.as_view(), name="books_list"),
    path("books/<int:pk>/", views.book_detail_view, name="book_detail"),
    path("books/create/", views.BookCreateView.as_view(), name="book_create"),
    path("books/<int:pk>/edit/", views.BookUpdateView.as_view(), name="book_update"),
    path("books/<int:pk>/delete/", views.BookDeleteView.as_view(), name="book_delete"),
]
