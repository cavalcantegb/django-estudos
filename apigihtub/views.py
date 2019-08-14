from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests 
from django.views import generic
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from . import services
from .models import User
import json

# Create your views here.
class APIGithubView(APIView):
    def post(self, request):
        username = request.data.get("username")
        response = services.get_user(self,username)
        if response is not None:
            message = response.name
            data = response.parse_user()
            return Response({"message":message, "data": data})
        else:
            message = "Fail"
        return Response({"message":message})