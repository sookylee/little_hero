from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from .models import Post
import django_filters
from .filters import *

# Create your views here.

# view when you click the title of post.
# you need regist_no and site_domain in query 
class PostViewDetail(generics.ListAPIView) :
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostDetailSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = PostDetailFilter


# default view of notice board
class PostViewAll(viewsets.ModelViewSet) :
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer


# query handling of notice board
class PostSearchView(generics.ListAPIView) :
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = PostFilter