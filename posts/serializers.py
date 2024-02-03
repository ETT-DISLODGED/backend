from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.nickname')

    class Meta:
        model = Post
        fields = ['id', 'author','level','title','tag','group','content','created_at','updated_at']