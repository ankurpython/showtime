from django.contrib import admin
from movieapp.models import Movie

# Register your models here.
admin.site.register(Movie)

class MovieAdmin(admin.ModelAdmin):
    list_display=['name','releasedate','actor','actress','rating','created','updated']
