from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.nickname')
    class Meta:
        model=Comment
        fields=['id','author','post','content','created_at','updated_at']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.nickname')
    comment = CommentSerializer(many=True, source='comments', read_only=True) #source=model의 related_name 명시해야 보임

    class Meta:
        model = Post
        fields = ['id', 'author','level','title','tag','group','content','created_at','updated_at','comment']

