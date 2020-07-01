from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post

# Create your views here.
class PostViewAll(viewsets.ModelViewSet) :
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer) :
        serializer.save(user=self.request.user)