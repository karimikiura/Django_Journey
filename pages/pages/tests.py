from urllib import response
from django.test import TestCase, SimpleTestCase


# SimpleTestCase -> used when no database is required.
class SimpleTestCase(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)