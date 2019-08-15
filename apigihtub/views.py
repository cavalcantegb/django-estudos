from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from . import services
from .models import User
import requests 
import json

# Create your views here.

####### Users
class UserGithubView(APIView):
    def get(self, request):
        username = request.data.get("username")
        response = services.get_user(self,username)
        if response is not None:
            message = response.name
            data = response.parse_user()
            return Response(data)
        else:
            message = "Fail"
        return Response({"message":message})

####### Repos    
class ReposGithubView(APIView):
    def get(self, request):
        username = request.data.get("username")
        response = services.get_repos(self,username)
        if response is not None:
            data = response.parse_repos()            
            return Response(data)
        else:
            message = "Fail"
        return Response({"message":message})
    
####### List Users
class UsersListGithubView(APIView):
    def get(self, request):
        page = request.data.get("page")
        per_page = request.data.get("per_page")
        response = services.list_users(page, per_page)
        if response is not None:
            data = response.parse_users()
            return Response(data)
        