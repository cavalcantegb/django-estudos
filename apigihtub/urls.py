from django.urls import path
from .views import UserGithubView, ReposGithubView, UsersListGithubView, UsersReposListGithubView

urlpatterns = [
    path('user/', UserGithubView.as_view()),
    path('users/', UsersListGithubView.as_view()),
    path('users-repos/', UsersReposListGithubView.as_view()),
    path('repos/', ReposGithubView.as_view()),   
]