from django.db import models


class Category(models.Model):
    name = models.CharField('Categories', max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name


class BookSearch(models.Model):
    name_of_book = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_book


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    cover_image = models.ImageField(upload_to='book_covers', blank=True, null=True)
    author = models.CharField(max_length=200)
    summary = models.TextField()
    category = models.ManyToManyField(Category, related_name='books')
    pdf = models.FileField(upload_to='pdfs')
    recommended_books = models.BooleanField(default=False)
    fiction_books = models.BooleanField(default=False)
    business_books = models.BooleanField(default=False)

    def __str__(self):
        return self.title
