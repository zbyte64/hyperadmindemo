from django.contrib import admin
from models import Workout, DataPoint

class DataInline(admin.TabularInline):
    model = DataPoint

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['excercise', 'calories']
    list_filter = ['endurance', 'strength', 'flexibility']
    inlines = [DataInline]

admin.site.register(Workout, WorkoutAdmin)

