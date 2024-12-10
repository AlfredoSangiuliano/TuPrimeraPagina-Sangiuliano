from django.db import models

# Create your models here.

class Cancion(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    year = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.title} - {self.author}"
    
class Disco(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    year = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.title} - {self.author}"
    
class Banda(models.Model):
    name = models.CharField(max_length=120)
    style = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    description = models.CharField(max_length=500, default='')
    def __str__(self):
        return f"{self.title} - {self.author}"
    

