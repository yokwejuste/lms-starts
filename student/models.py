from django.db import models

# Create your models here.


class Register(models.Model):
    username = models.CharField(max_length=150, default="John Doe")
    email = models.EmailField()
    password = models.CharField(max_length=300)
    date_of_birth = models.DateTimeField()
    sex = models.CharField(max_length=6, default="Unknown")


class Login(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=300)


class Online(models.Model):
    status = models.BooleanField(default=True)
