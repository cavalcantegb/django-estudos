from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UserSerializer, RepoSerializer
from . import services
from .models import User, Repo
import requests 
import json

# Create your views here.

####### Users
class UserGithubView(APIView):
    def get(self, request):
        username = request.data.get("username")
        response = services.get_user(self,username)
        if response is not None:
            message = response.username
            data = response.parse_user()
            return Response(data)
        else:
            message = "Fail"
        return Response({"message":message})

    def post(self, request):
        user_data = request.data
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User {} created successfully".format(user_saved.username)})

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
    
    def post(self, request):
        users = request.data.get("users")
        for item in users:
            response = services.get_user(self, item['user'])
            if response is not None:
                user = response.parse_user()
                serializer = UserSerializer(data=user)
                if serializer.is_valid(raise_exception=True):
                    try:
                        user_saved = serializer.save()
                    except:
                        pass
                    response_repos = services.get_repos(self, item['user'])
                    repos = response_repos.parse_repos()
                    for repo in repos['repos']:
                        repo_serializer = RepoSerializer(data=repo)
                        if repo_serializer.is_valid(raise_exception=True):
                            try:              
                                repo_saved = repo_serializer.save()
                            except:
                                pass
        return Response({"data": "Sucesss"})
                
            