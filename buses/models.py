from django.contrib.gis.db import models 
from django.utils import timezone

# Create your models here.


class BusStation(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326,null=True,blank=True)
    address = models.CharField(max_length=50)
    bus_station_id=models.CharField(max_length=10)
    objects=models.Manager()



class Timings(models.Model):
	bus_station_id=models.ForeignKey(BusStation,on_delete=models.CASCADE,default=1)
	arrival_time=models.TimeField(default=timezone.now())      

	def __str__(self):
		return self.bus_station_id.name, self.arrival_time


