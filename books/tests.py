from django.contrib.auth import get_user_model 
from django.test import TestCase
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
        self.assertEqual(f'{self.book.price}',"12")

    def test_book_list_view(self):
        response=self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"harry potter")
        self.assertTemplateUsed(response,"books/book_list.html")

    def book_detail_view(self):
        response=self.client.get(self.book. get_absolute_url())
        no_response=self.client.get('/books/64896518446')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'harry potter')
        self.assertContains(response,'An excellent review')
        self.assertTemplateUsed(response,"books/book_detail.html")




            