from django.contrib import admin

from .models import Book, Comment, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "cost"]


admin.site.register(Book, BookAdmin)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ["name"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Category, CategoryAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["book", "text", "user"]
