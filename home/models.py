from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

class HealthRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

class DietList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dietician = models.CharField(max_length=100)
