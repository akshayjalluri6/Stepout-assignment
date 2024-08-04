from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Train(models.Model):
    DAYS_OF_WEEK = (
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    )

    TrainNumber = models.IntegerField(primary_key=True)
    TrainName = models.CharField(max_length=50)
    CoachCount = models.IntegerField()
    TotalSeats = models.IntegerField()
    AvailableSeats = models.IntegerField()
    Days = MultiSelectField(choices=DAYS_OF_WEEK)

    def save(self, *args, **kwargs):
        if self.AvailableSeats is None:
            self.AvailableSeats = self.TotalSeats
        super().save(*args, **kwargs)

class Station(models.Model):
    StationName = models.CharField(max_length=50)
    StationCode = models.IntegerField(primary_key=True)
    PlatformCount = models.IntegerField()

    def __str__(self):
        return self.StationName
    
class Route(models.Model):
    RouteId = models.IntegerField(primary_key=True)
    TrainNumber = models.ForeignKey(Train, on_delete=models.CASCADE)
    StationCode = models.ForeignKey(Station, on_delete=models.CASCADE)
    ArrivalTime = models.TimeField()
    DepartureTime = models.TimeField()
    Date = models.DateField()

    def __str__(self):
        return str(self.RouteId)

class Booking(models.Model):
    BookingId = models.IntegerField(primary_key=True)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    BookingDate = models.DateField(auto_now_add=True)
    BookingTime = models.TimeField(auto_now_add=True)
    RouteId = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.BookingId)
