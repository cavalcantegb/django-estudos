from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.test import TestCase

# Create your tests here.

class BaseViewTest(APITestCase):
    client = APIClient()
    
    @staticmethod
    def create_song(title="", artist=""):
        if title != "" and artist != "":
            Songs.objects.create(title=title, artist=artist)
            
    def setUp(self):
        # add test data
        self.create_song("Jurassic Park", "Steven Spielberg")
        
class GetAllSongTest(BaseViewTest):
    
    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        return null        
