from django.test import TestCase

# Create your tests here.
class SearchFormTestCase(TestCase):
    def test_empty_get(self):
        response = self.client.get('/en/dev/search/', HTTP_HOST='modnicy.com.ua:8000')
        self.assertEqual(response.status_code, 200)