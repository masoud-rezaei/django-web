from .views import HomepageView, AboutpageView
from django.test import SimpleTestCase
from django.urls import reverse, resolve

# Create your tests here.


class testHomepageview(SimpleTestCase):

    def test_statuscode(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_urlname(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_homepage_contain_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "Homepage")

    def test_homepage_contain_not_correct_html(self):
        response = self.client.get("/")
        self.assertNotContains(response, "homepage")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomepageView.as_view().__name__)


class AboutePageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboute_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_about_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_url_resolve(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutpageView.as_view().__name__)
