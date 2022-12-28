from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class U(models.Model):
    usr = models.ForeignKey(User,on_delete=models.CASCADE)
    login = models.CharField(max_length=10)
    logout = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.usr.username}"

class Mails(models.Model):
    usr = models.ForeignKey(User,on_delete=models.CASCADE)
    reciver = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.usr.username}"
