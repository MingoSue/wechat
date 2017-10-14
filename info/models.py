from django.db import models

# Create your models here.
class User(models.Model):
    openid = models.CharField(max_length=200)
    nickname = models.CharField(max_length=20)
    sex = models.CharField(max_length=3)
    province = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)

class Code(models.Model):
    code = models.CharField(max_length=200)
