from django.db import models

# Create your models here.
class Movie (models.Model):
    tittle = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=25, null=False)   
    director = models.CharField(max_length=50, null=False)
    year_realease = models.IntegerField(null=False)
    sinopsis = models.TextField(null=False)
    
    def __str__(self) -> str:
        return self.tittle