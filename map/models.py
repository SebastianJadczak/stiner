from django.db import models

from trails.models import Trail


class Point(models.Model):

    TYPE_POINT = (
        ('Zamek', 'Zamek'),
        ('Kościół', 'Kościół')
    )

    name = models.CharField(max_length=30)
    descriptions = models.TextField()
    location = models.CharField(max_length=30)
    coordinateX = models.DecimalField(max_length=30, decimal_places=7, max_digits=100)
    coordinateY = models.DecimalField(max_length=30, decimal_places=7, max_digits=100)
    image = models.ImageField(upload_to='media/img_point/%Y/%m%d')
    type = models.CharField(max_length=10, choices=TYPE_POINT)
    trails = models.ManyToManyField(Trail, blank=True)

    def __str__(self):
        return self.name
