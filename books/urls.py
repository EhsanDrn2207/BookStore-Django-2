from django.urls import path, include
from django.urls import re_path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .api_views import BookViewSet, CommentViewSet, CategoryViewSet 


from . import views

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
   path('api/', include(router.urls)),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path("books/<int:pk>/", views.book_detail_view, name="book_detail"),
   path("books/create/", views.BookCreateView.as_view(), name="book_create"),
   path("books/<int:pk>/edit/", views.BookUpdateView.as_view(), name="book_update"),
   path("books/<int:pk>/delete/", views.BookDeleteView.as_view(), name="book_delete"),
   path("", views.BooksListView.as_view(), name="books_list"),
]
