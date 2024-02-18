from rest_framework import serializers
from .models import User

# class SignUpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('__all__')
#         extra_kwargs = {"password": {"write_only":True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()

#         return user

class SignUpSerializer(serializers.Serializer):
    class Meta:
        model=User
        fields=['id', 'username','password','nickname', 'email', 'gender', 'age']
        extra_kwargs = {"password": {"write_only":True}}

    gender_list = (
        ('남', '남'),
        ('여', '여')
    )

    username = serializers.CharField(max_length=20) # 아이디
    password = serializers.CharField()
    email = serializers.EmailField()
    nickname = serializers.CharField(max_length=8) # 이름
    gender = serializers.ChoiceField(
        choices=gender_list
    )
    age = serializers.IntegerField()

    def create(self, validated_data):

        if User.objects.filter(username=validated_data['username']).exists() or User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError('username 존재 or email 존재')


        else:
            user = User.objects.create(
                username=validated_data['username'],
                nickname=validated_data['nickname'],
                email=validated_data['email'],
                gender=validated_data['gender'],
                age=validated_data['age']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user

class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields=['id', 'username','password','nickname', 'email', 'gender', 'age']
        extra_kwargs = {"password": {"write_only":True}}

    gender_list = (
        ('남', '남'),
        ('여', '여')
    )

    username = serializers.CharField(max_length=20) # 아이디
    password = serializers.CharField()
    email = serializers.EmailField()
    nickname = serializers.CharField(max_length=8) # 이름
    gender = serializers.ChoiceField(
        choices=gender_list
    )
    age = serializers.IntegerField()


    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise serializers.ValidationError('잘못된 비밀번호입니다.')
        else:
            raise serializers.ValidationError('존재하지 않는 사용자입니다.')
        
        data = {
            'id': user.id,
            'username':user.username,
            'nickname' : user.nickname,
            'email' : user.email,
            'gender' : user.gender,
            'age' : user.age,
        }

        return data
    

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields=['id', 'username','nickname', 'email', 'gender', 'age']

    gender_list = (
        ('남', '남'),
        ('여', '여')
    )

    username = serializers.CharField(max_length=20) # 아이디
    email = serializers.EmailField()
    nickname = serializers.CharField(max_length=8) # 이름
    gender = serializers.ChoiceField(
        choices=gender_list
    )
    age = serializers.IntegerField()

class PasswordUpdateSerializer(serializers.Serializer):
    current_password = serializers.CharField(max_length=128, write_only=True)
    new_password = serializers.CharField(max_length=128, write_only=True)
    


    