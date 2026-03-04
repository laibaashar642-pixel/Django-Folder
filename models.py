from django.db import models

# Create your models here.
# this is a file where we make schema a means structure to create a tables so jo datbase hai wo backened ka heart hai
#hamay kisi bhi cheez ka agr hamay kisi bhi student ka data pta hona chaye structure bnanay kai liya aur usi structure ko isis file mai likhty hai
class Student(models.Model):# models is a class that we import
   #aik field jo haiwo django automatically khud add krta hai jissy hum primary key kehty hai
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=10)
    age=models.IntegerField(null=True,blank=True)
    email=models.EmailField()
    address=models.TextField()
    image=models.ImageField()
    file=models.FileField()


class Product(models.Model):
    name=models.CharField(max_length=10)
    price=models.IntegerField()
    description=models.TextField()
    image=models.ImageField()
    file=models.FileField()
#initial .py wali file mai do important parts hai pehala dependency jis mai agr hum models mai change laty hai tu phir hum dubara run kry gai tu intial 2py wali file aye ghi aur us kai underlikha ho gha kai ye intiall1 sai bhi data le rhi agr hhum 1 wali file ko delete kr dai gai tu database collapse ho jye gha interview ka sbsy important sawal hai operation means alter krna hai kia operations perform krna

# Create your models here.

