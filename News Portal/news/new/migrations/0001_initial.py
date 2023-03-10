# Generated by Django 4.1.7 on 2023-03-12 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_rating', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('SP', 'Спорт'), ('CI', 'Кино'), ('PO', 'Политика'), ('EC', 'Экономика')], max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(choices=[('AR', 'Статья'), ('NE', 'Новость')], max_length=2)),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('reit_post', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new.category')),
                ('post_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='Category_post',
            field=models.ManyToManyField(through='new.PostCategory', to='new.category'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new.author'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_com', models.TextField()),
                ('time_com', models.DateTimeField(auto_now_add=True)),
                ('reit_com', models.IntegerField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
