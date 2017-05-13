from django.db import models

class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=22, unique=True)
    balance = models.IntegerField(default=0)

class Bank(models.Model):
    id = models.AutoField(primary_key=True)
    jackpot = models.BigIntegerField(default=0)