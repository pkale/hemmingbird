from django.db import models

# Create your models here.
class Songs(models.Model):
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)


class Person(models.Model):
    # song title
    name = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    gender = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)


class Customer(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=60)
    gender = models.CharField(max_length=1,default='', choices=GENDER)
    height = models.IntegerField(default=0)
    sleeve_length = models.IntegerField(default=0)
    waist_length = models.IntegerField(default=0)
    shoulder_length = models.IntegerField(default=0)

    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Tailor(models.Model):
    LOCATIONS = (
        ('V', 'Vietnam'),
        ('T', 'Thailand'),
        ('S', 'Singapore'),
    )
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=1,default='', choices=LOCATIONS)
    capacity = models.IntegerField(default=0)


class Order(models.Model):
    ITEMS = (
        ('1', 'Dress 1'),
        ('2', 'Dress 2'),
        ('3', 'Dress 3'),
    )
    FABRICS = (
        ('P', 'Polyester'),
        ('C', 'Cotton'),
        ('R', 'Raeyon'),
    )
    COLORS = (
        ('B', 'Black'),
        ('G', 'Gray'),
        ('B', 'Navy Blue'),
        ('R', 'Red'),

    )
    customer_name = models.CharField(max_length=60)
    order_number = models.IntegerField(default=0)
    item = models.CharField(max_length=1,default='', choices=ITEMS)
    color = models.CharField(max_length=1,default='', choices=COLORS)
    fabric = models.CharField(max_length=1,default='', choices=FABRICS)

    order_time = models.IntegerField(default=0)




