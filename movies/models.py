from django.db import models
from django.db.models.deletion import CASCADE

class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    db_table = 'actors'



class Movie(models.Model):
    title = models.CharField(max_length=150)
    released_date = models.DateField()
    runtime = models.IntegerField()
    actors = models.ManyToManyField(Actor, through='Actor_Movie')

    db_table = 'movies'


class Actor_Movie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=CASCADE)
    movie = models.ForeignKey(Movie, on_delete=CASCADE)

    db_table = 'actors_movies'