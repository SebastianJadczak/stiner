# Generated by Django 3.0.4 on 2020-08-16 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0022_auto_20200816_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion_about_point',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
