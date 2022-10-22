from django.urls import resolve
from django.test import TestCase
from trailer_bookings.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # reolve is a function that takes a URL and returns a 
        # function that Django will use to build the page
        found = resolve('/')
        # We're checking that Django found the func called home_page
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Trailer Bookings</title>', html)
        self.assertTrue(html.endswith('</html>'))