from urllib.request import urlopen
import json
from .utils import Payload

url_user = "https://api.github.com/users/"

def get_user(self, username):
    try:
        return Payload(urlopen(url_user + username).read().decode('utf-8'))
    except:
        return None