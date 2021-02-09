# Generated by Django 3.1.2 on 2021-02-08 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
        ('trails', '0007_trail_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='points',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.point'),
        ),
    ]