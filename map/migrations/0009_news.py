# Generated by Django 3.1.2 on 2021-05-05 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_auto_20210430_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='media/img_news/%Y/%m%d')),
                ('descriptions', models.TextField()),
            ],
        ),
    ]