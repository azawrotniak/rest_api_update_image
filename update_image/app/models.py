from django.contrib.auth.models import User
from django.db import models

# Create your models here.
ACCOUNT_CHOICES = (
    (1, "Basic"),
    (2, "Premium"),
    (3, "Enterprise"),
)


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.IntegerField(choices=ACCOUNT_CHOICES)