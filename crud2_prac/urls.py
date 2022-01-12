from django.urls import path, include

urlpatterns = [
    path('', include('owner_dog.urls')),
    path('', include('movies.urls')),
]
