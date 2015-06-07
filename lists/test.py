from django.test import TestCase
from django.http import HttpRequest

from .views import home_page

# create your test


class HomePageViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn('<title>To-Do lists</title>', response.content.decode('utf8'))
        self.assertTrue(response.content.startswith('<html>'))
        self.assertTrue(response.content.endswith('</html>'))
