from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your models here.
from django.core.validators import MinValueValidator
from django.urls import reverse



from new.recv import POSITIONS

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        self.post_set.all().aggregate(post_rating=Sum('post_rating') * 3)
        self.user.comment_set.all().aggregate(com_rating=Sum('comment_rating'))
        Author.objects.filter(author_rating=Sum(post__author=self.id))
        self.save()

    def __str__(self):
        return f'{self.user}'



class Category(models.Model):
    sport = 'SP'
    cinema = 'CI'
    politica= 'PO'
    economy= 'EC'
    category = models.CharField(max_length=2, choices=POSITIONS, unique=True)
    subscriber = models.ManyToManyField(User, blank=True, null=True)

class Post(models.Model):
    artic = 'AR'
    news = 'NE'
    TYP = [
        (artic, 'Статья'),
        (news, 'Новость'),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # news = models.BooleanField(default=True)
    typ = models.CharField(max_length=2, choices=TYP)
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    reit_post = models.IntegerField(default=0)
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

    def __str__(self):
        return f'{self.title.title()}: {self.text[:10]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class PostCategory(models.Model):
    post_cat = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_cat = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.category_cat}:{self.post_cat}'




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # text_com = models.CharField(max_length=255, unique=True)
    text_com = models.TextField()
    time_com = models.DateTimeField(auto_now_add=True)
    reit_com = models.IntegerField(default=0)
    def like(self):
        self.reit_com += 1
        self.save()
        return self.reit_com

    def dislike(self):
        self.reit_com -= 1
        self.save()
        return self.reit_com

    def __str__(self):
        return f'{self.text_com}'

