from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from uuid import uuid4

class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(default=uuid4,primary_key=True, unique=True)
    email = models.EmailField(unique=True,max_length=200)
    name = models.CharField(max_length=200)

    USERNAME_FIELD="email"

class Token(models.Model):
    key = models.UUIDField(default=uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
