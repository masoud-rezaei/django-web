from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(db_index=True,max_length=200)
    description = models.TextField(max_length=10000,null=True,blank=True)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover=models.FileField(upload_to='covers/',blank=True)

    class Meta:
        indexes=[models.Index(fields=['title'],name='title_index'),
        ]
        permissions =[('special_status','can read all books'),
        ]
    
    def __str__(self):
        return self.title
    def get_absolute_url(self): 
        return reverse('book_detail', kwargs={'pk':str(self.pk)})

class Review(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reviews',)
    review=models.CharField(max_length=220)
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)

    def __str__(self):
        return self.review 