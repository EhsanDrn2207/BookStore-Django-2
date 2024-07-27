from django.forms import ModelForm

from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'cost', 'cover']
