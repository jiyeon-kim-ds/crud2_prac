from django.db import models
from django.db.models.deletion import CASCADE

class Owner(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=255, unique=True)
    age = models.IntegerField()
    
    class Meta:
        db_table = 'owners'


class Dog(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        db_table = 'dogs'

