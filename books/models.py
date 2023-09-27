from django.db import models
from authentication.models import User

class Book(models.Model):
    id= models.BigAutoField(primary_key=True)
    title= models.CharField(max_length=200,)
    content=models.CharField(max_length=500)
    author= models.ForeignKey(User,on_delete=models.CASCADE)
