from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True, null=False)
    username = models.CharField(max_length=50, null=False)
    url = models.CharField(max_length=100, null=False)

    def __str__(self):
        return "Github User: " + self.username

class Repo(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    html_url = models.CharField(max_length=200, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return "Github Repo: " + self.name
    
    @property
    def repo_owner(self):
        return self.owner.username
