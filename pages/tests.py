from django.test import TestCase

# Create your tests here.
# tests where you do not use a database would be Simple Test Case.
# tests where you need a test datbase use TestCase. 

from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location_homepageview(self): 
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Home")
        