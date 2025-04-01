from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    perex = models.TextField()
    content = models.TextField()
    date = models.DateTimeField()
    categories = models.ManyToManyField(Category, related_name='articles')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.title[:20]
    