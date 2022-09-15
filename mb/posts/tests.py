from django.test import TestCase
from django.urls import reverse

from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title="Sublime or Vs Code?", text="Code editor wars.")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_text = f'{post.text}'
        self.assertEqual(expected_object_text, 'Code editor wars.')

class PostTitleTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Sublime or Vs Code?", text="Code editor wars.")

    def test_post_title(self):
        post = Post.objects.get(id=1)
        expected_object_text = f'{post.title}'
        self.assertEqual(expected_object_text, 'Sublime or Vs Code?')


class HomePageViewTest(TestCase):

    def setUp(self) :
        Post.objects.create(title="Cloud wars", text="AWS leads GCP and Azure to dominate the cloud market")
    
    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')


