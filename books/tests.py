from http import client
from urllib import response
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import Permission
from django.test import TestCase ,Client
from django.urls import reverse
from.models import Book ,Review
# Create your tests here.

class BookTest(TestCase):

    def setUp(self):
        self .user=get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@gmail.com',
            password='testpass123'
        )
        self.apecial_permission =Permission.objects.get(codename="special_status")
        self.book=Book.objects.create(
            title='harry potter',
            author='jk rowling',
            price='10.00',
        )
        self.review=Review.objects.create(
            book=self.book,
            author=self.user,
            review='an excellent review ',
        )
  

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}',"harry potter")
        self.assertEqual(f'{self.book.author}',"jk rowling")
        self.assertEqual(f'{self.book.price}',"10.00")

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email='reviewuser@email.com', password='testpass123')
        response=self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"harry potter")
        self.assertTemplateUsed(response,"books/book_list.html")

    def book_detail_view_with_permissions(self):
        self.client.login(email="reviewer@email.com",password="testpass123")
        self.user.user_permissions.add(self.special_permissions)
        response=self.client.get(self.book. get_absolute_url())
        no_response=self.client.get('/books/64896518446')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'harry potter')
        self.assertContains(response,'An excellent review')
        self.assertTemplateUsed(response,"books/book_detail.html")

    def test_book_list_view_for_logged_out_user(self): 
        self.client.logout()
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response, '%s?next=/books/' % (reverse('account_login')))
        response=self.client.get('%s?next=/books/' % (reverse('account_login')))
        self.assertContains(response,'Log In')




            