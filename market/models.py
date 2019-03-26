from django.db import models
from django.urls import reverse

# Create your models here.


class BuySell(models.Model):
    userName = models.CharField(max_length=250, default=" ")
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=500)
    contact = models.CharField(max_length=100)
    image = models.FileField()

    def get_absolute_url(self):
        return reverse('market:buysell')

    def __str__(self):
        return self.name+" "+self.contact


class Lost(models.Model):
    userName = models.CharField(max_length=250, default=" ")
    ItemName = models.CharField(max_length=250)
    OwnerName = models.CharField(max_length=500)
    contact = models.CharField(max_length=100)
    image = models.FileField()

    def get_absolute_url(self):
        return reverse('market:lost')

    def __str__(self):
        return self.ItemName + " " + self.contact


class Found(models.Model):
    userName = models.CharField(max_length=250, default=" ")
    ItemName = models.CharField(max_length=250)
    FinderName = models.CharField(max_length=500)
    contact = models.CharField(max_length=100)
    image = models.FileField()

    def get_absolute_url(self):
        return reverse('market:found')

    def __str__(self):
        return self.ItemName + " " + self.contact


class Rent(models.Model):
    userName = models.CharField(max_length=250, default=" ")
    ItemName = models.CharField(max_length=250)
    Rentee = models.CharField(max_length=500)
    contact = models.CharField(max_length=100)
    image = models.FileField()

    def get_absolute_url(self):
        return reverse('market:rent')

    def __str__(self):
        return self.ItemName + " " + self.contact


class To_Let(models.Model):
    userName = models.CharField(max_length=250, default=" ")
    ItemName = models.CharField(max_length=250)
    OwnerName = models.CharField(max_length=500)
    contact = models.CharField(max_length=100)
    ChargesPerDay = models.CharField(max_length=100)
    image = models.FileField()

    def get_absolute_url(self):
        return reverse('market:to_let')

    def __str__(self):
        return self.ItemName + " " + self.contact

