from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import AllowAny
from rest_framework.generics import UpdateAPIView

from posts.models import *
from posts.serializers import *
from rest_framework.pagination import PageNumberPagination
from .pagination import PaginationHandlerMixin

# pagination을 위한 함수
class MypagePagination(PageNumberPagination):
    page_size = 6


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
        
    def patch(self, request):
        user = get_object_or_404(User, id=request.user.id)
        serializer = LoginSerializer(user)
        return Response({'message': '현재 로그인된 유저 정보 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)

#로그아웃 함수
class LogoutView(APIView):

    def post(self, request):
        response = Response({
            "message": "로그아웃 성공"
        }, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie('refresh')
        response.delete_cookie('access')

        return response
    
# 유저 정보 수정 함수
class UserUpdateView(UpdateAPIView):

    def get(self, request, format=None):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        return Response({'message': '로그인 후 이용 가능합니다.'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        
        if serializer.is_valid():
            if User.objects.filter(username=request.POST.get('username')).exists() or User.objects.filter(email=request.POST.get('email')).exists():
                return Response({'message': 'username or email 존재'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'message': '유저 변경 성공.', 'data': serializer.validated_data}, status=status.HTTP_200_OK)
        return Response({'message': '유저 변경 실패.', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    


# 비밀번호 변경
class PasswordUpdateView(APIView):
    serializer_class = PasswordUpdateSerializer

    def patch(self, request, format=None):
        serializer = PasswordUpdateSerializer(data=request.data)
        
        if serializer.is_valid():
            user = request.user
            current_password = serializer.validated_data['current_password']
            new_password = serializer.validated_data['new_password']

            # 현재 비밀번호 확인
            if not user.check_password(current_password):
                return Response({'message': '현재 비밀번호가 옳지 않습니다.'}, status=HTTP_400_BAD_REQUEST)

            # 새로운 비밀번호 설정
            user.set_password(new_password)
            user.save()

            return Response({'message': '비밀번호가 성공적으로 변경되었습니다.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': '데이터를 바르게 입력해주세요.'}, status=status.HTTP_400_BAD_REQUEST)
        

class MyPostView(APIView, PaginationHandlerMixin): # 내가 작성한 게시글 가져오기
    pagination_class = MypagePagination

    def get(self, request):
        # page_number = self.request.query_params.get('page', 1)

        myPosts = Post.objects.filter(author=request.user).order_by('-created_at')
        myPosts = self.paginate_queryset(myPosts)
        myPosts_serializers = [PostSerializer(post).data for post in myPosts]

        #total_posts = Post.objects.filter(author=request.user).count()

        total_posts = Post.objects.filter(author=request.user).count()
        total_pages = self.paginator.page.paginator.num_pages if self.paginator else 0
        current_page = self.paginator.page.number if self.paginator and self.paginator.page else 1


        response_data = {
            'total': total_posts,
            'total_page': total_pages,
            'current_page': current_page,
            '내가 작성한 게시물': myPosts_serializers,
        }

        return Response(response_data)