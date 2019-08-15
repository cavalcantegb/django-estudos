from django.urls import path
from .views import UserGithubView, ReposGithubView, UsersListGithubView

urlpatterns = [
    path('user/', UserGithubView.as_view()),
    path('users/', UsersListGithubView.as_view()),
    path('repos/', ReposGithubView.as_view()),   
]