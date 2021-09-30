from django.db import models


# Create your models here.
class Vechile(models.Model):
    unit = models.CharField(max_length=200, primary_key=True)
    mileage = models.IntegerField()
    manufacture = models.CharField(max_length=200)
    status = models.BooleanField()


class vechile_Mileage(models.Model):
    id = models.IntegerField(auto_created=True ,primary_key=True)
    unit = models.ForeignKey(Vechile, default="1",on_delete=models.SET_DEFAULT ,null=True)
    day_mileage = models.IntegerField(null =True)
    date = models.CharField(max_length=200,null =True)
