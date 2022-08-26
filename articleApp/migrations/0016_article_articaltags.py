# Generated by Django 3.2.15 on 2022-08-23 08:21

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('articleApp', '0015_article_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='articaltags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
