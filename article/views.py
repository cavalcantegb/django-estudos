from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles":serializer.data})

    def post(self, request):
        article = request.data.get('article')
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})
    
    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' update successfully".format(article_saved.title)})

    def delete(self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        print(article)
        article.delete()
        return Response({"success": "Article '{}' delete successfully".format(article.title)})