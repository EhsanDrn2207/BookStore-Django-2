from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=6, decimal_places=3)
    cover = models.ImageField(upload_to="covers/", blank=True)
    publisher = models.CharField(max_length=50, blank=True)
    translator = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.id])


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    recommend = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
