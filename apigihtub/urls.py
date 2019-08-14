from django.urls import path
from .views import APIGithubView

urlpatterns = [
    path('api-github/', APIGithubView.as_view())
]