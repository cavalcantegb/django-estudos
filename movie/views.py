from django.shortcuts import render
from rest_framework import generics
from .models import Movie
from .serializers import MoviesSerializer

# Create your views here.
class ListMoviesView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer

