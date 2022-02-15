from django.urls import reverse, resolve
from django.test import TestCase
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from .views import SignupPageView
# Create your tests here.


class CustomuserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='masoud',
            email="mas@email.com",
            password='ramz1234'
        )
        self.assertEqual(user.username, 'masoud')
        self.assertEqual(user.email, 'mas@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='masbbbbboud',
            email="ma5555s@email.com",
            password='ramz555551234'
        )
        self.assertEqual(admin_user.username, 'masbbbbboud')
        self.assertEqual(admin_user.email, 'ma5555s@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):  # new
    def setUp(self):

        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):

        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self):  # new
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):  # new
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
