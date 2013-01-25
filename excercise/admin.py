from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline
from models import Workout, DataPoint, TaggedItem

class DataInline(admin.TabularInline):
    model = DataPoint

class TaggedItemInline(GenericTabularInline):
    model = TaggedItem

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['excercise', 'calories']
    list_filter = ['endurance', 'strength', 'flexibility']
    inlines = [DataInline, TaggedItemInline]

admin.site.register(Workout, WorkoutAdmin)

