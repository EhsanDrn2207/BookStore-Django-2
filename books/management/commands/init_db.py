import os
import shutil
from random import choice
from tqdm import tqdm
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

from books.models import Category, Book


User = get_user_model()
PASSWORD = "abcd1234"

class Command(BaseCommand):
    def handle(self, *args, **options):
        
        media_folder = os.path.join(settings.MEDIA_ROOT, 'covers')
        
        if os.path.exists(media_folder):
            for filename in os.listdir(media_folder):
                file_path = os.path.join(media_folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)  
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path) 
                except Exception as e:
                    print(f"error occured while deleting {file_path}: {e}")
                    
        Category.objects.all().delete()
        Book.objects.all().delete()
        User.objects.all().delete()
        
        User.objects.create_superuser(username="admin", password="1234")

        users = []
        for i in tqdm (range(1, 11), 'users'):
            user = User.objects.create_user(f"user{i}", password=PASSWORD)
            users.append(user)
        
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
                publisher = f"publisher{i}", 
                translator = f"trasnlator{i}",
                category = choice(categories)
            )