# -*- encoding: utf-8 -*-
# ! python3

from django.test import Client, TestCase
from django.urls import reverse


class UrlsClientTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_admin_login_screen(self):
        response = self.client.get(reverse("admin:index"), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_default_page(self):
        response = self.client.get(reverse("web:default_page"), follow=False)
        self.assertEqual(response.status_code, 200)
