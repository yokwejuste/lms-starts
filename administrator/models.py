from django.db import models

# Create your models here.


class Student(models.Model):
    full_name = models.CharField(max_length=200)
    identity = models.IntegerField()
    level = models.PositiveIntegerField()
