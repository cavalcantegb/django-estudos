from urllib.request import urlopen
import json
from .utils import PayloadList, PayloadDict

url_user = "https://api.github.com/users"
url_repo = ""

def get_user(self, username):
    try:
        return PayloadDict(urlopen(url_user + "/" + username).read().decode('utf-8'))
    except:
        return None

def get_repos(self, username):
    try:
        return PayloadList(urlopen(url_user + "/" + username + "/repos").read().decode('utf-8'))
    except:
        return None

def list_users(page = 1, per_page = 1):
    try:
        query_string = "?page={}&per_page={}".format(page, per_page)
        #https://api.github.com/users
        return PayloadList(urlopen(url_user + query_string).read().decode('utf-8'))
    except:
        return None
    