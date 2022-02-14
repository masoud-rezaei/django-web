from .views import HomepageView
from django.test import SimpleTestCase
from django.urls import reverse , resolve

# Create your tests here.
class testHomepageview(SimpleTestCase):

    def test_statuscode(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_urlname(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_template(self):
        response=self.client.get("/")    
        self.assertTemplateUsed(response,"home.html")

    def test_homepage_contain_correct_html(self):
        response=self.client.get("/")
        self.assertContains(response,"Homepage")    
    def test_homepage_contain_not_correct_html(self):
        response=self.client.get("/")
        self.assertNotContains(response,"homepage")    

    def test_homepage_url_resolves_homepageview(self): 
        view=resolve('/')
        self.assertEqual(view.func.__name__,HomepageView.as_view().__name__)  
