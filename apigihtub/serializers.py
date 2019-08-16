from rest_framework import serializers
from .models import User, Repo

class UserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    username = serializers.CharField()
    url = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
class RepoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    html_url = serializers.CharField()
    owner = serializers.IntegerField()
    
    def create(self, validated_data):
        return Repo.objects.create(**validated_data)

