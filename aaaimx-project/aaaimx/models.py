from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=30, unique=True)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    fanpage = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    division = models.ForeignKey(Division, blank=True, null=True, on_delete=models.SET_NULL)
    birthdate = models.DateField(blank=True, null=True)

