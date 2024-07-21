from django.test import TestCase
from django.shortcuts import reverse

from .models import Book


class BooksTestCase(TestCase):

    def setUp(self):
        self.book1 = Book.objects.create(
            title="title1",
            description='text1',
            author='author1',
            cost=111.111,
        )

    def test_book_list_view(self):
        self.assertEqual(self.book1.title, 'title1')
        self.assertEqual(self.book1.description, 'text1')
        self.assertEqual(self.book1.author, 'author1')
        self.assertEqual(self.book1.cost, 111.111)

    def test_book_list_url(self):
        response = self.client.get("/books/list/")
        self.assertEqual(response.status_code, 200)

    def test_book_list_url_name(self):
        response = self.client.get(reverse('books_list'))
        self.assertEqual(response.status_code, 200)

    def test_book_list_components(self):
        response = self.client.get(reverse('books_list'))
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book1.description)
        self.assertContains(response, self.book1.author)

    def test_book_list_template_used(self):
        response = self.client.get(reverse('books_list'))
        self.assertTemplateUsed(response, "books/books_list.html")

