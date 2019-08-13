from django.urls import path
from .views import ListMoviesView

urlpatterns = [
    path('movies/', ListMoviesView.as_view(), name="movies-all")
]