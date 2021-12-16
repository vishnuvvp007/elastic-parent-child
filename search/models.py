from django.db import models

# Create your models here.

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=50)

class BookType(models.Model):
    book_type = models.CharField(max_length=20) # Hard Cover, Soft Cover, Kindle Edition, Digital PDF etc.

class Book(models.Model):
    book_title = models.TextField()
    book_types = models.ManyToManyField(BookType, through='BookPrice', through_fields=('book', 'book_type'))

class BookPrice(models.Model):
    book_type = models.ForeignKey(BookType, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
