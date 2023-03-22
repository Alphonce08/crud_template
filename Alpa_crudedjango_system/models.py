from django.db import models

class People(models.Model):
    Name = models.CharField(max_length=30, blank=False, null=False)
    Email = models.CharField(max_length=30, blank=False, null=False)
    Age = models.IntegerField(max_length=30, blank=False, null=False)
    Gender = models.CharField(max_length=30, blank=False, null=False)
    Phonenumber = models.CharField(max_length=30, blank=False, null=False)
    Amount = models.IntegerField(max_length=30, blank=False, null=False)