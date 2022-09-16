# Django_Journey
This repo contains simple and complex Django App that I Implement while learning Django web framework

## Projects
# HelloWorld App
This is a simple hello world app in Django.\
Learned to:
- Create function based views
- Use HttpResponse to return http request to client

```python
    fun homePageView(requests):
        return HttpResponse("Hello, World)
```

# Pages App
A simple app that has two pages. The `index` and `about.html` pages.\
Learned how to return these pages using `class based views`.
```python
    from django.views.generic import TemplateVew
    class HomePageView(TemplateView):
        template_name = 'home.html'
```

Learnt to create simple _test cases_ for the basic app.\
_"Code without tests is broken as designed"~J.Kaplan Moss_ \
Used `SimpleTestCase` that lets testing without lookup on the database.
```python
from django.test import impleTestCase

class SimpleTestCase(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
```
To run the tests, run:\
`python manage.py test`

# Message Board
A simple app that implements models with SQLite database. Uses the TemplateView to List all Posts stored in the database using `TestCase`.\
The app also tests the following\
1. PostModel
```python
class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title="Sublime or Vs Code?", text="Code editor wars.")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_text = f'{post.text}'
        self.assertEqual(expected_object_text, 'Code editor wars.')
```
2. PostTitle
```python
class PostTitleTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Sublime or Vs Code?", text="Code editor wars.")

    def test_post_title(self):
        post = Post.objects.get(id=1)
        expected_object_text = f'{post.title}'
        self.assertEqual(expected_object_text, 'Sublime or Vs Code?')
```
3. HomePageView
```python
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
```
**9/15/2022**
