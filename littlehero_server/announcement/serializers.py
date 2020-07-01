from rest_framework import serializers, generics
from .models import Post
from django_filters import rest_framework as filters

class PostSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Post
        fields = '__all__'
        read_only_fields = '__all__'
        #light_only_fields=(
        # )
