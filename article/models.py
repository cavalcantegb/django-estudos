from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
