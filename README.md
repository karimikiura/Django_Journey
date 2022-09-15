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
A simple app that has two pages. The `index` and `about.html` pages.
Learned how to return these pages using `class based views`.
```python
    from django.views.generic import TemplateVew
    class HomePageView(TemplateView):
        template_name = 'home.html'
```

Learnt to create simple _test cases_ for the basic app.
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

**9/15/2022**
