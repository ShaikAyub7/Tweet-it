# Generated by Django 5.0.7 on 2024-08-09 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_tweet_follwers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='follwers',
        ),
    ]
