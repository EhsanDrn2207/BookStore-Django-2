from django.contrib import admin

from .models import Book, Comment


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "cost"]


admin.site.register(Book, BookAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["book", "text", "user"]
