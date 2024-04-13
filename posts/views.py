from .serializers import *
from .permissions import AuthenticatedOnly, IsAuthor
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# pagination을 위한 함수
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 10000

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    permission_classes = [IsAuthenticated, AuthenticatedOnly]
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["group"]


    def perform_create(self, serializer):
        # 이미지 저장을 위한 것
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
        total_posts = (Post.objects.filter(author=self.request.user).count())%11
        image_url = image_list[total_posts][0]

        serializer.save(author = self.request.user, image=image_url)

class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, author_voice=self.request.user.user_voice)




# tts 코드
from django.http import HttpResponse
from rest_framework.views import APIView
from google.cloud import texttospeech

import boto3
from dislodged_project.settings import ACCESS_KEY_ID, SECRET_ACCESS_KEY, AWS_REGION, AWS_STORAGE_BUCKET_NAME, AWS_S3_CUSTOM_DOMAIN, DEFAULT_FILE_STORAGE


class Mp3Upload(APIView):
    # 댓글 전체 조회
    def post(self, request, post_pk, format=None):
        comments = Comment.objects.filter(post_id=post_pk).order_by('created_at') # 게시글 댓글 가져오고 오래된 순으로

        comment_list = [{
            "comment_id": comment.id,
            "speed": comment.author_voice.speed,
            "pitch": comment.author_voice.pitch,
            "type": comment.author_voice.type,
            "content": comment.content
        } for comment in comments]

        if len(comment_list)==0:
            return Response({"RESULT": "변환할 댓글이 없습니다."}, status=400)
        
        s3_client = boto3.client(
            's3',
            aws_access_key_id=ACCESS_KEY_ID,
            aws_secret_access_key=SECRET_ACCESS_KEY
        )
        
        mp3_list = s3_client.list_objects(Bucket=AWS_STORAGE_BUCKET_NAME, Prefix="mp3/"+str(post_pk)+"/") # s3 버켓 가져와서
        content_list = mp3_list['Contents'] # contents 가져오기! 
        file_list = []
        for content in content_list:
            key = content['Key'] # Key값(파일명)만 뽑기
            file_list.append(key)


        for i in range(len(file_list), len(comment_list)):
            client = texttospeech.TextToSpeechClient()
            synthesis_input = texttospeech.SynthesisInput(text=comment_list[i].get('content'))
            voice = texttospeech.VoiceSelectionParams(
                language_code="ko-KR", name=comment_list[i].get('type')
            )
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3,
                pitch=comment_list[i].get('pitch'), 
                speaking_rate=comment_list[i].get('speed') 
            )

            response = client.synthesize_speech(
                input=synthesis_input,
                voice=voice,
                audio_config=audio_config
            )
            s3_client = boto3.client(
                's3',
                aws_access_key_id=ACCESS_KEY_ID,
                aws_secret_access_key=SECRET_ACCESS_KEY
            )

            s3_client.put_object(Body=response.audio_content, Bucket=AWS_STORAGE_BUCKET_NAME, Key="mp3/"+str(post_pk)+"/"+str(i)+".mp3")


        return Response({"RESULT": comment_list, "반영된 댓글수": len(comment_list)-len(file_list)}, status=200)
    
    def put(self, request, post_pk, format=None):
        comments = Comment.objects.filter(post_id=post_pk).order_by('created_at') # 게시글 댓글 가져오고 오래된 순으로

        comment_list = [{
            "comment_id": comment.id,
            "speed": comment.author_voice.speed,
            "pitch": comment.author_voice.pitch,
            "type": comment.author_voice.type,
            "content": comment.content
        } for comment in comments]
        

        for i in range(len(comment_list)):
            client = texttospeech.TextToSpeechClient()
            synthesis_input = texttospeech.SynthesisInput(text=comment_list[i].get('content'))
            voice = texttospeech.VoiceSelectionParams(
                language_code="ko-KR", name=comment_list[i].get('type')
            )
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3,
                pitch=comment_list[i].get('pitch'), 
                speaking_rate=comment_list[i].get('speed') 
            )

            response = client.synthesize_speech(
                input=synthesis_input,
                voice=voice,
                audio_config=audio_config
            )
            s3_client = boto3.client(
                's3',
                aws_access_key_id=ACCESS_KEY_ID,
                aws_secret_access_key=SECRET_ACCESS_KEY
            )

            s3_client.put_object(Body=response.audio_content, Bucket=AWS_STORAGE_BUCKET_NAME, Key="mp3/"+str(post_pk)+"/"+str(i)+".mp3")


        return Response({"RESULT": comment_list}, status=200)
    
    def get(self, request, post_pk, format=None):
        comments = Comment.objects.filter(post_id=post_pk)    

        s3_client = boto3.client(
            's3',
            aws_access_key_id=ACCESS_KEY_ID,
            aws_secret_access_key=SECRET_ACCESS_KEY
        )

        mp3_list = s3_client.list_objects(Bucket=AWS_STORAGE_BUCKET_NAME, Prefix="mp3/"+str(post_pk)+"/") # s3 버켓 가져와서
        content_list = mp3_list['Contents'] # contents 가져오기! 
        file_list = []
        for content in content_list:
            key = content['Key'] # Key값(파일명)만 뽑기
            file_list.append(key)
        # print(len(file_list)-len(comments))

        if len(comments)==0:
            return Response({"RESULT": "댓글을 달아주세요!"}, status=400)
        elif str(post_pk) not in ''.join(file_list): # 변환하지 않은 댓글이 있다면
            return Response({"RESULT": "음성 변환을 먼저 해주세요!"}, status=400)
        
        
        data = []
        for i in range(len(comments)):
            url = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.ap-northeast-2.amazonaws.com/"+"mp3/"+str(post_pk)+"/"+str(i)+".mp3" # 이렇게 url 가져오기
            data.append(url)        

        return Response({"RESULT": data}, status=200)
    


class TextToSpeechAPIView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        text = request.query_params.get('text', None)
        speed = float(request.query_params.get('speed', None))
        pitch = float(request.query_params.get('pitch', None))
        type = request.query_params.get('type', None)

        if not text:
            return HttpResponse("No text provided", status=400)
        

# Google TTS 처리
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="ko-KR", name=type # type인데....어케할까 일단 아는게 "ko-KR-Wavenet-D"
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16,
            pitch=pitch, # 0, -20.0~20.0 사이만 가능
            speaking_rate=speed # 1, 0.25~4.0 사이만 가능
        )

        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )
    
# 음성 파일을 HttpResponse 객체로 반환
        return HttpResponse(response.audio_content, content_type="audio/wav")
    