from django.db import models
from django.contrib.auth.models import User
# from django.db import Sum

from news.recv import POSITIONS

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.FloatField(default=0.0)

class Category(models.Model):
    sport = 'SP'
    cinema = 'CI'
    politica= 'PO'
    economy= 'EC'
    category_tema = models.CharField(max_length=2, choices=POSITIONS, unique=True)


class Post(models.Model):
    artic = 'AR'
    new = 'NE'
    TYP = [
        (artic, 'Статья'),
        (new, 'Новость'),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # news = models.BooleanField(default=True)
    typ = models.CharField(max_length=2, choices=TYP)
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    reit_com = models.FloatField(default=0.0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    Category_post = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.reit_com += 1
        self.save()

    def dislike(self):
        self.reit_com -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:124]}...'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # text_com = models.CharField(max_length=255, unique=True)
    text_com = models.TextField()
    time_in_com = models.DateTimeField(auto_now_add=True)
    reit_com = models.FloatField(default=0.0)
    def like(self):
        self.reit_com += 1
        self.save()

    def dislike(self):cd
        self.reit_com -= 1
        self.save()
