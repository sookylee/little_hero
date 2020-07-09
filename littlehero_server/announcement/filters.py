from django_filters import rest_framework as fils
from rest_framework import generics
from .models import Post

class PostDetailFilter(fils.FilterSet) :
    registNo = fils.NumberFilter(field_name='regist_no')
    siteDomain = fils.NumberFilter(field_name='site_domain')

    class Meta :
        model = Post
        fields = ['registNo', 'siteDomain']
