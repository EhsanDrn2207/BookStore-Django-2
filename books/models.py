from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=6, decimal_places=3)
