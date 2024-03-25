from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


# Create your models here.


class User(AbstractUser):

    gender_list = (
        ('남', '남'),
        ('여', '여')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20, unique=True) 
    nickname = models.CharField(max_length=8)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=2, choices=gender_list, default='여')
    age = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(80)])

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'nickname', 'email', 'gender', 'age']

    

    def __str__(self):
        return f'{self.username}'
    
    
class Voice_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    speed = models.FloatField(default=0)
    pitch = models.FloatField(default=1)
    type = models.CharField(max_length=100, default="ko-KR-Standard-A") # textfield는 default 지정이 안됨.

    def __str__(self):
        return f'{self.user} voice_info'