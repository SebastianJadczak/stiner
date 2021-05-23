# Generated by Django 3.1.2 on 2021-05-18 21:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_trails', '0010_auto_20210503_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertrail',
            name='done',
            field=models.ManyToManyField(blank=True, related_name='done_your_trail', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usertrail',
            name='heart',
            field=models.ManyToManyField(blank=True, related_name='heart_your_trail', to=settings.AUTH_USER_MODEL),
        ),
    ]