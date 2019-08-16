from rest_framework import serializers
from .models import User, Repo

class UserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    username = serializers.CharField()
    url = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
class RepoSerializer(serializers.Serializer):
    class Meta:
        model = Repo
        fields = ('id', 'name', 'html_url', 'owner')
    
