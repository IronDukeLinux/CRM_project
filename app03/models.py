from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=9, decimal_places=2)


class User(models.Model):
    pass


class Role(models.Model):
    pass


class Permission(models.Model):
    pass


class User2Role(models.Model):
    pass


class Role2Permission(models.Model):
    pass
