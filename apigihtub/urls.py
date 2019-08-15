from django.urls import path
from .views import UserGithubView, ReposGithubView

urlpatterns = [
    path('user/', UserGithubView.as_view()),
    path('repos/', ReposGithubView.as_view()),
    
]