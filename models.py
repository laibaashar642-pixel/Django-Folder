from django.db import models

# Create your models here.
class Recepie(models.Model):
    Recepie_name=models.CharField(max_length=100)
    Recepie_quantity=models.IntegerField