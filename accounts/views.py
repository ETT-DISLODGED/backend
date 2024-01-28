from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import AllowAny


# Create your views here.

class SignupView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '회원가입 성공', 'data': serializer.data}, status=HTTP_200_OK)
        return Response({'message': '회원가입 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = User.objects.all()
        serializer = SignUpSerializer(users, many=True)
        return Response({'message': '유저 목록 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)


#로그인 함수
class LoginView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        user = get_object_or_404(User, id=request.user.id)
        serializer = LoginSerializer(user)
        return Response({'message': '현재 로그인된 유저 정보 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)

    def post(self, request):
        user = authenticate(
            username=request.data.get("username"), password=request.data.get("password")
        )
        if user is not None:
            serializer = LoginSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    'message': '로그인 성공',
                    "user": serializer.data,
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res
        else:
            return Response({'message': '로그인 실패'}, status=status.HTTP_400_BAD_REQUEST)

#로그아웃 함수
class LogoutView(APIView):

    def post(self, request):
        response = Response({
            "message": "로그아웃 성공"
        }, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie('refresh')
        response.delete_cookie('access')

        return response