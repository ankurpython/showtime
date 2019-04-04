from django.db import models
from django.utils import timezone
# Create your models here.
class Movie(models.Model):
    moviename=models.CharField(max_length=64)
    image=models.ImageField(upload_to='images',blank=True,null=True)
    content=models.TextField(null=True)
    releasedate=models.DateField()
    actor=models.CharField(max_length=30)
    actress=models.CharField(max_length=30)
    rating=models.IntegerField()
    director=models.CharField(max_length=30,null=True)
    producer=models.CharField(max_length=30,null=True)
    #image=models.ImageField(default='default.jpg',upload_to='pics')
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.moviename
