from django.db import models


# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    number = models.IntegerField()
    male = models.CharField(max_length=250)
    female = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    parent_selection = models.CharField(max_length=250)
    child_selection = models.CharField(max_length=250)
    savingaccount = models.CharField(max_length=250)
    currentaccount = models.CharField(max_length=250)
    joinaccount = models.CharField(max_length=250)
    demataccount = models.CharField(max_length=250)
    debitcard = models.CharField(max_length=250)
    creditcard = models.CharField(max_length=250)
    chequebook = models.CharField(max_length=250)


def __str__(self):
    return self.name
