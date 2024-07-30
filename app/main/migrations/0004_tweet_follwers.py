# Generated by Django 5.0.7 on 2024-07-24 11:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_whatsnew_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='follwers',
            field=models.ManyToManyField(blank=True, related_name='follwers', to=settings.AUTH_USER_MODEL),
        ),
    ]