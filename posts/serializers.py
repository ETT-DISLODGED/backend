from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source='author.id')
    author_nickname = serializers.ReadOnlyField(source = 'author.nickname')
    author_username = serializers.ReadOnlyField(source='author.username') # username (아이디)추가
    voice_speed = serializers.ReadOnlyField(source='author_voice.speed') # 댓글 작성자 voice 정보들 가져오기. voice_info가 바뀌면 이것도 바뀐다.
    voice_pitch = serializers.ReadOnlyField(source='author_voice.pitch')
    voice_type = serializers.ReadOnlyField(source='author_voice.type')

    is_liked = serializers.BooleanField(default=False)

    class Meta:
        model=Comment
        fields=['id','author_id', 'author_nickname','author_username','voice_speed','voice_pitch','voice_type','post','content','created_at','updated_at', 'is_liked']



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
    author_nickname = serializers.ReadOnlyField(source='author.nickname') #
    comment = CommentSerializer(many=True, source='comments', read_only=True) #source=model의 related_name 명시해야 보임
    
    
    image_url = serializers.ReadOnlyField(source='image') # 이미지

    class Meta:
        model = Post
        fields = ['id', 'author_id', 'author_nickname','image_url','title','tag','group','content','created_at','updated_at','comment']

