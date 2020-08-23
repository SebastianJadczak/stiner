# Generated by Django 3.0.4 on 2020-08-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0018_opinion_about_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion_about_point',
            name='amount_rating',
            field=models.DecimalField(decimal_places=1, max_digits=5, max_length=10),
        ),
        migrations.AlterField(
            model_name='opinion_about_point',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=5, max_length=10),
        ),
    ]