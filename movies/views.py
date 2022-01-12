import json

from django.views import View
from django.http  import JsonResponse

from .models import Actor, Movie

class ActorView(View):
    
