# Generated by Django 3.1.2 on 2020-11-14 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0009_auto_20201102_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bought_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bought_by', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
