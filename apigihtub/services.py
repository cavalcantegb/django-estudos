from urllib.request import urlopen
import json
from .utils import PayloadUser, PayloadRepo

url_user = "https://api.github.com/users/"
url_repo = ""

def get_user(self, username):
    try:
        return PayloadUser(urlopen(url_user + username).read().decode('utf-8'))
    except:
        return None

def get_repos(self, username):
    try:
        return PayloadRepo(urlopen(url_user + username + "/repos").read().decode('utf-8'))
    except:
        return None