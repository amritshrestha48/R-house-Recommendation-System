from django.contrib import admin
from .models import Movie,Rating

# Register your models here.
@admin.register(Movie)
class movieAdmin(admin.ModelAdmin):
    list_display=('id','title','genres')

@admin.register(Rating)
class ratingAdmin(admin.ModelAdmin):
    list_display=('user','movie','rating')