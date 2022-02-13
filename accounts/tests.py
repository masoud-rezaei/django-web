import email
from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class CustomuserTest(TestCase):

    def test_create_user(self):
        User=get_user_model()
        user=User.objects.create_user(
            username='masoud',
            email="mas@email.com",
            password='ramz1234'
        )
        self.assertEqual(user.username,'masoud')
        self.assertEqual(user.email,'mas@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User=get_user_model()
        admin_user=User.objects.create_superuser(
            username='masbbbbboud',
            email="ma5555s@email.com",
            password='ramz555551234'
        )
        self.assertEqual(admin_user.username,'masbbbbboud')
        self.assertEqual(admin_user.email,'ma5555s@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        
