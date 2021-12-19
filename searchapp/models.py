from django.db import models

class search (models.Model) :
    search = models.CharField
    time  = models.DateTimeField()
    year = models.CharField(max_length=20)
