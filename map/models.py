from django.contrib.auth.models import User
from django.db import models

class Galery(models.Model):
    """Model odpowiadający galerii zdjęć konkretnego punktu."""
    name = models.CharField(max_length=30)
    image1 = models.ImageField(upload_to='media/img_point/%Y/%m%d', blank=True)
    image2 = models.ImageField(upload_to='media/img_point/%Y/%m%d', blank=True)
    image3 = models.ImageField(upload_to='media/img_point/%Y/%m%d', blank=True)
    image4 = models.ImageField(upload_to='media/img_point/%Y/%m%d', blank=True)
    image5 = models.ImageField(upload_to='media/img_point/%Y/%m%d', blank=True)

    def __str__(self):
        return self.name


class Point(models.Model):

    TYPE_POINT = (
        ('Zamki', 'Zamki'),
        ('Forty', 'Forty'),
        ('Kościoły', 'Kościoły'),
        ('Muzeum', 'Muzeum'),
        ('Parki', 'Parki'),
        ('Ogrody', 'Ogrody'),
        ('Pomniki', 'Pomniki'),
        ('Rynki', 'Rynki'),
        ('Mosty', 'Mosty'),
        ('Wieże', 'Wieże'),
        ('Stadiony', 'Stadiony'),
        ('Cmentarze', 'Cmentarze'),
        ('Budowle', 'Budowle'),
        ('Porty', 'Porty'),
        ('Filcharmonie', 'Filcharmonie')
    )

    COUNTRY = (
        ('Polska','Polska'),
        ('Niemcy', 'Niemcy'),
        ('Czechy', 'Czechy'),
        ('Słowacja', 'Słowacja'),
        ('Rosja', 'Rosja'),
        ('Ukraina', 'Ukraina'),
        ('Białoruś', 'Białoruś'),
        ('Litwa', 'Litwa'),
        ('Estonia', 'Estonia'),
        ('Włochy', 'Włochy'),
        ('Izrael', 'Izrael')
    )
    REGION = (
        ('Góry','Góry'),
        ('Pojezierze','Pojezierze'),
        ('Morze','Morze'),
        ('Nizinny', 'Nizinny')
    )

    name = models.CharField(max_length=30)
    descriptions = models.TextField()
    country = models.CharField(max_length=15, choices=COUNTRY, default='Polska')
    location = models.CharField(max_length=30)
    region = models.CharField(max_length=15, choices=REGION, default='Nizinny')
    address = models.CharField(max_length=40, default=' ')
    coordinateX = models.DecimalField(max_length=30, decimal_places=7, max_digits=100)
    coordinateY = models.DecimalField(max_length=30, decimal_places=7, max_digits=100)
    image = models.ImageField(upload_to='media/img_point/%Y/%m%d')
    type = models.CharField(max_length=15, choices=TYPE_POINT)
    more_info = models.CharField(max_length=70, default=' ')
    gallery = models.ManyToManyField(Galery)

    def __str__(self):
        return self.name

class Opinion_about_Point(models.Model):
    """Model opisujący opinie o Punkcie."""
    user = models.CharField(max_length=30)
    opinion = models.CharField(max_length=530)
    rating = models.IntegerField()
    point = models.ForeignKey(Point, blank=True, on_delete=models.CASCADE)

class Coordinates(models.Model):
    """Model opisujący położenie miast."""
    name = models.CharField(max_length=30)
    coordinateX = models.DecimalField(max_length=30, decimal_places=7, max_digits=100)
    coordinateY = models.DecimalField(max_length=30, decimal_places=7, max_digits=100)

    def __str__(self):
        return self.name


class NewsletterEmail(models.Model):
    """Model odpowiadający za zapisanych użytkowników do newslettera."""
    email = models.EmailField()

class News(models.Model):
    """Model odpowiedzialny za nowości na stronie."""
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/img_news/%Y/%m%d')
    descriptions = models.TextField()

    def __str__(self):
        return self.title