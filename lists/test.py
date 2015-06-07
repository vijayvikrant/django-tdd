from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from .views import home_page

# create your test

class HomePageViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn('<title>To-Do lists</title>', response.content.decode('utf8'))
        self.assertTrue(response.content.startswith('<html>'))
        self.assertTrue(response.content.strip().endswith('</html>'))


# as much as possible, the tests needs to test behaviour

# instead of checking if the title has something, we could
# check if the home_page_view is rendering the right template
# the template is a sort of constant. so redundant to test it.
        template = render_to_string('home.html')
        self.assertEqual(
            response.content.decode('utf8'),
            template.decode('utf8')
        )
