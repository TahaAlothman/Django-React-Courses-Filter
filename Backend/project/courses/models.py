from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    image = models.ImageField(upload_to='courses')
    price = models.IntegerField()
