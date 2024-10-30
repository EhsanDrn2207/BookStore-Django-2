from django.forms import ModelForm

from .models import Book, Comment


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'category', 'publisher', 'translator', 'cost', 'cover']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text", "recommend"]