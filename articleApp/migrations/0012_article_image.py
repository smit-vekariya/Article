# Generated by Django 3.2.15 on 2022-08-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleApp', '0011_article_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images'),
        ),
    ]