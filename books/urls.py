from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
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

schema_view = get_schema_view(
   openapi.Info(
      title="Library API",
      default_version='v1',
      description="API documentation for the personal library project",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]