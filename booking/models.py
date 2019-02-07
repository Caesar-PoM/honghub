from django.db import models

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=30, blank=True)
    floor = models.IntegerField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    vc = models.BooleanField(default=False)
    projector = models.BooleanField(default=False)
    chair_number = models.PositiveIntegerField()
    tel_num = models.CharField(max_length=10)

    def __str__(self):
        return self.name + ', Flr.' + str(self.floor) + ', ' + self.building.name


class TimeSlot(models.Model):
    time_slot = models.CharField(max_length=5)

    def __str__(self):
        return self.time_slot


class Username(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    tel_num = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.username


class Meeting(models.Model):
    subject = models.CharField(max_length=50)
    meeting_date = models.DateField('date booked')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time_slot = models.TimeField()
    stop_time_slot = models.TimeField()
    period = models.TimeField()
    username = models.ForeignKey(Username, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
