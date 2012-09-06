from django.db import models

class Workout(models.Model):
    excercise = models.CharField(max_length=100)
    minutes = models.IntegerField()
    calories = models.IntegerField()
    endurance = models.BooleanField()
    strength = models.BooleanField()
    flexibility = models.BooleanField()
    gps_track = models.FileField(upload_to='workouts/')

