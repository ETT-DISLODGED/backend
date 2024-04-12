from django.db import models
from accounts.models import User, Voice_Info
import uuid

# Create your models here.

class Post(models.Model):
    
    level_list = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]

    group_list = [
        ('진로', '진로'),
        ('연애', '연애'),
        ('가족/친구', '가족/친구'),
        ('기타', '기타')
    ]
    image_list = [ # (DB에 저장되는 값, 사용자에게 보여지는 값)
        ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL1.jpg', 1),
        ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL2.jpg', 2),
        ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL3.jpg', 3),
        ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL4.jpg', 4),
        ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL5.jpg', 5),
        ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL6.jpg', 6),
        ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL7.jpg', 7),
        ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL8.jpg', 8),
        ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL9.jpg', 9),
        ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL10.jpg', 10),
        ('https://dislodged.s3.ap-northeast-2.amazonaws.com/DL11.jpg', 11)

    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)  # 게시글 작성자
    title = models.CharField(max_length=20)
    tag = models.CharField(max_length=8)
    group = models.CharField(max_length=16, choices=group_list) # 게시판 유형
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=128, choices=image_list, default = 'https://dislodged.s3.ap-northeast-2.amazonaws.com/DL1.jpg') # 이미지 객체 URL

    def __str__(self):
        return f'[{self.id}]{self.title} :: {self.author}'

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_voice = models.ForeignKey(Voice_Info, on_delete=models.CASCADE, null=True) # 댓글 작성자의 Voice_Info
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.id}]{self.post.title} :: {self.author}'