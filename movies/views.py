import json

from django.views import View
from django.http  import JsonResponse

from .models import Actor, Movie, Actor_Movie

class ActorView(View):
    def get(self, request):
        """
            OUTPUT : {
        "first_name" : first_name,
        "last_name" : last_name,
        "movies" : [{"title" : moive_title},{"title2" : moive_title2},...]
        }
        """
        actors = Actor.objects.all()
        results = []

        for actor in actors:
            actors_movies_set = Actor_Movie.objects.filter(actor_id=actor.id)
            actor_dict = {
                "first_name" : actor.first_name,
                "last_name" : actor.last_name,
                "movies" : [{"title" : actors_movies_set.movie.title} for actors_movies_set in actors_movies_set]
            }
            results.append(actor_dict)
        
        return JsonResponse({"actors" : results}, status = 200)