from urllib import response
from django.contrib.auth import get_user_model 
from django.test import TestCase, Client
from django.urls import reverse

from .models import Post

class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='nkarimi',
            email='nkarimi@blog.com',
            password='test12345'
        )

        self.post = Post.objects.create(
            title = "Expression of Interest",
            body = "Investor facilitation is a time consuming task.",
            author = self.user,
        )

    def test_string_representation(self):
        post = Post(title="A hackable editor")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Expression of Interest')
        self.assertEqual(f'{self.post.author}', 'nkarimi')
        self.assertEqual(f'{self.post.body}', 'Investor facilitation is a time consuming task.')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, "Investor facilitation is a time consuming task.")
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1')
        no_response = self.client.get('/post/20000/')
        # TODO -> Fix asserion error. SOLVED by removing trailing slash on post id ->'/post/1'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Expression of Interest')
        self.assertTemplateUsed(response, 'post_detail.html')

    
    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1')

    def test_post_create_view(self):
        response = self.client.post(reverse('post-new'), {
            'title': 'Absolute URL',
            'body': "Django absolute url",
            'author': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Absolute URL')
        self.assertContains(response, 'Django absolute url')


    def test_post_update_view(self):
        response = self.client.post(reverse('post-update', args='1'),{
            'title': 'Updated Absolute URL',
            'body': 'Updated Django absolute url',
        })

        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.get(reverse('post-delete', args='1'))
        self.assertEqual(response.status_code, 200)

    