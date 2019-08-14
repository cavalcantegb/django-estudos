from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests 
from django.views import generic
from rest_framework.decorators import api_view
from .serializers import UserSerializer

# Create your views here.
class APIGithubView(APIView):
    def post(self, request):
        username = request.data.get("username")
        
        url = "https://api.github.com/users/"
        if (len(username) > 0):
            url = url + username
            response = requests.get(url)
            usuario = response.json()
            serializer = UserSerializer(data=usuario)
            if serializer.is_valid(raise_exception=True):
                return Response({"message":serializer.data})
        else:
            return Response({"message":"User not found"})    
        return Response({"message":"We were not able to complete your request."})   
        