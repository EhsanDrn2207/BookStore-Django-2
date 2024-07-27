from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class SignUpPageTest(TestCase):
    def test_signup_page_url(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_page_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_template_used(self):
        response = self.client.get(reverse("signup"))
        self.assertTemplateUsed(response, "registration/signup_page.html")

    def test_signup_page_form(self):
        username = "new_username"
        email = "new_email"
        user = get_user_model().objects.create_user(username=username, email=email)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].email, email)
        self.assertEqual(get_user_model().objects.all()[0].username, username)
