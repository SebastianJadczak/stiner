# Generated by Django 3.1.2 on 2021-05-07 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0006_auto_20210507_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trail',
            old_name='watched',
            new_name='done',
        ),
    ]