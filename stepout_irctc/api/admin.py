from django.contrib import admin

from .models import Train, Station, Route, Booking


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('TrainNumber', 'TrainName', 'CoachCount', 'TotalSeats', 'AvailableSeats', 'Days')

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('StationName', 'StationCode', 'PlatformCount')

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('RouteId', 'TrainNumber', 'StationCode', 'ArrivalTime', 'DepartureTime', 'Date')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('BookingId', 'UserId', 'BookingDate', 'BookingTime', 'RouteId')
