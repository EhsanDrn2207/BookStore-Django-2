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
        response = self.client.get("")
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

    def test_book_detail_view(self):
        self.assertEqual(self.book1.title, 'title1')
        self.assertEqual(self.book1.description, 'text1')
        self.assertEqual(self.book1.author, 'author1')
        self.assertEqual(self.book1.cost, 111.111)

    def test_book_detail_url(self):
        response = self.client.get(f'/books/{self.book1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_book_detail_url_name(self):
        response = self.client.get(reverse("book_detail", args=[self.book1.id]))
        self.assertEqual(response.status_code, 200)

    def test_book_detail_template_used(self):
        response = self.client.get(reverse('book_detail', args=[self.book1.id]))
        self.assertTemplateUsed(response, "books/book_detail.html")

    def test_book_detail_components(self):
        response = self.client.get(reverse('book_detail', args=[self.book1.id]))
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book1.description)
        self.assertContains(response, self.book1.author)
        self.assertContains(response, self.book1.cost)

    def test_get_object_or_404_page(self):
        response = self.client.get(reverse('book_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_book_create_url(self):
        response = self.client.get("/books/create/")
        self.assertEqual(response.status_code, 200)

    def test_book_create_name(self):
        response = self.client.get(reverse("book_create"))
        self.assertEqual(response.status_code, 200)

    def test_book_create_view(self):
        response = self.client.post(path=reverse("book_create"), data={
            "title": "title2",
            "description": 'text2',
            "author": 'author2',
            "cost": 222.222,
            }
        )
        self.assertEqual(Book.objects.last().title, 'title2')
        self.assertEqual(Book.objects.last().description, 'text2')
        self.assertEqual(Book.objects.last().author, 'author2')
        self.assertEqual(float(Book.objects.last().cost), 222.222)
        self.assertEqual(response.status_code, 302)

    def test_book_create_template_used(self):
        response = self.client.get(reverse('book_create'))
        self.assertTemplateUsed(response, "books/book_create.html")

    def test_book_update_url(self):
        response = self.client.get(f"/books/{self.book1.id}/edit/")
        self.assertEqual(response.status_code, 200)

    def test_book_update_name(self):
        response = self.client.get(reverse("book_update", args=[self.book1.id]))
        self.assertEqual(response.status_code, 200)

    def test_book_update_template_used(self):
        response = self.client.get(reverse("book_update", args=[self.book1.id]))
        self.assertTemplateUsed(response, "books/book_update.html")

    def test_book_update_view(self):
        response = self.client.post(path=(reverse("book_update", args=[self.book1.id])), data={
            "title": "title3",
            "description": "text3",
            "author": "author3",
            "cost": 333.333,
        })
        self.assertEqual(Book.objects.first().title, "title3")
        self.assertEqual(Book.objects.first().description, "text3")
        self.assertEqual(Book.objects.first().author, "author3")
        self.assertEqual(float(Book.objects.first().cost), 333.333)
        self.assertEqual(response.status_code, 302)

    def test_book_delete_url(self):
        response = self.client.get(f'/books/{self.book1.id}/delete/')
        self.assertEqual(response.status_code, 200)

    def test_book_delete_name(self):
        response = self.client.get(reverse("book_delete", args=[self.book1.id]))
        self.assertEqual(response.status_code, 200)

    def test_book_delete_template_used(self):
        response = self.client.get(reverse("book_delete", args=[self.book1.id]))
        self.assertTemplateUsed(response, "books/book_delete.html")

    def test_book_delete_view(self):
        response = self.client.post(path=(reverse("book_delete", args=[self.book1.id])))
        self.assertEqual(response.status_code, 302)
