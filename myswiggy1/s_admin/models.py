from django.db import models

class Adminlogin(models.Model):
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    otp=models.IntegerField()

class StateModel(models.Model):
    state_no=models.AutoField(primary_key=True)
    state_name=models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.state_name

class CityModel(models.Model):
    city_no = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=30)
    state=models.ForeignKey(StateModel,on_delete=models.CASCADE)
    def __str__(self):
        return self.city_name
class AreaModel(models.Model):
    area_no = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=30)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)