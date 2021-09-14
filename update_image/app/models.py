from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=16, unique=True, blank=False)
    size_small = models.SmallIntegerField(default=200)
    size_large = models.SmallIntegerField(default=400)

    def __str__(self):
        return self.name


class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
