from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Workout(models.Model):
    excercise = models.CharField(max_length=100)
    minutes = models.IntegerField()
    calories = models.IntegerField()
    endurance = models.BooleanField()
    strength = models.BooleanField()
    flexibility = models.BooleanField()
    gps_track = models.FileField(upload_to='workouts/')

class DataPoint(models.Model):
    workout = models.ForeignKey(Workout)
    data = models.TextField()

class TaggedItem(models.Model):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.tag
