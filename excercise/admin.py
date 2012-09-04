from django.contrib import admin
from models import Workout

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['excercise', 'calories']
    list_filter = ['endurance', 'strength', 'flexibility']

admin.site.register(Workout, WorkoutAdmin)

