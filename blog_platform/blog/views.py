from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import BlogPost, Comment, Category
from .serializers import BlogPostSerializer, CommentSerializer, CategorySerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
