from random import choice
from tqdm import tqdm
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from books.models import Publisher, Category, Book


User = get_user_model()
PASSWORD = "abcd1234"

class Command(BaseCommand):
    def handle(self, *args, **options):
        Publisher.objects.all().delete()
        Category.objects.all().delete()
        Book.objects.all().delete()
        User.objects.all().delete()
        
        User.objects.create_superuser(username="admin", password="1234")

        users = []
        for i in tqdm (range(1, 11), 'users'):
            user = User.objects.create_user(f"user{i}", password=PASSWORD)
            users.append(user)

        publishers = []
        for i in tqdm (range(1, 11), 'publishers'):
            publisher = Publisher.objects.create(name=f"publisher{i}")
            publishers.append(publisher)
        
        categories = []
        for i in tqdm (range(1, 11), 'categories'):
            category = Category.objects.create(name=f"category{i}")
            categories.append(category)

        for i in tqdm (range(1, 21), 'books'):
            book = Book.objects.create(
                user = choice(users),
                title = f"title{i}",
                description = f"description{i}",
                author = f"author{i}",
                cost = 999.999,
                publisher = choice(publishers), 
                translator = f"trasnlator{i}",
                category = choice(categories)
            )