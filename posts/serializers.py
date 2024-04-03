from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source='author.id')
    author = serializers.ReadOnlyField(source = 'author.nickname')
    class Meta:
        model=Comment
        fields=['id','author_id', 'author','post','content','created_at','updated_at']


class PostSerializer(serializers.ModelSerializer):

    # image_list = [ # (DB에 저장되는 값, 사용자에게 보여지는 값)
    #     ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL1.jpg', 1),
    #     ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL2.jpg', 2),
    #     ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL3.jpg', 3),
    #     ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL4.jpg', 4),
    #     ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL5.jpg', 5),
    #     ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL6.jpg', 6),
    #     ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL7.jpg', 7),
    #     ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL8.jpg', 8),
    #     ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL9.jpg', 9),
    #     ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL10.jpg', 10),
    #     ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL11.jpg', 11)

    # ]

    author_id = serializers.ReadOnlyField(source='author.id')
    author = serializers.ReadOnlyField(source='author.nickname')
    comment = CommentSerializer(many=True, source='comments', read_only=True) #source=model의 related_name 명시해야 보임
    
    image_url = serializers.ReadOnlyField(source='image') # 이미지

    class Meta:
        model = Post
        fields = ['id', 'author_id', 'author','image_url','level','title','tag','group','content','created_at','updated_at','comment']

