# from django.contrib import admin

# # Register your models here.
# from django.contrib.gis.admin import OSMGeoAdmin
# from .models import BusStation,Timings

# @admin.register(BusStation)
# class ShopAdmin(OSMGeoAdmin):
#     list_display = ('name', 'location')

# admin.site.register(Timings)


from django.contrib import admin

# from django.contrib.gis.admin import OSMGeoAdmin
from .models import BusStation,Timings

# @admin.register(BusStation)
# class BusStationAdmin(OSMGeoAdmin):
# 	list_display = ('name', 'location')
from leaflet.admin import LeafletGeoAdmin

# admin.site.register(BusStation, LeafletGeoAdmin)
@admin.register(BusStation)
class BusStationAdmin(LeafletGeoAdmin):
	list_display=('name', 'location')

admin.site.register(Timings)