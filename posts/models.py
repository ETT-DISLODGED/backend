from django.db import models
from accounts.models import User
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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)  # 게시글 작성자
    level=models.IntegerField(choices=level_list) # 심각도
    title = models.CharField(max_length=20)
    tag = models.CharField(max_length=8)
    group = models.CharField(max_length=16, choices=group_list) # 게시판 유형
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.id}]{self.title} :: {self.author}'