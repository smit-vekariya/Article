# Generated by Django 3.2.15 on 2022-08-29 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleApp', '0015_article_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]