# Generated by Django 3.0.5 on 2020-05-20 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0012_auto_20200520_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='coordinateX',
            field=models.DecimalField(decimal_places=5, max_digits=100, max_length=30),
        ),
        migrations.AlterField(
            model_name='point',
            name='coordinateY',
            field=models.DecimalField(decimal_places=5, max_digits=100, max_length=30),
        ),
    ]
