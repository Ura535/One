# Generated by Django 4.1.7 on 2023-03-30 11:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subscriber',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
