from .serializers import *
from .permissions import AuthenticatedOnly, IsAuthor
from rest_framework.permissions import IsAuthenticated

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
        serializer.save(author = self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# tts 코드
from django.http import HttpResponse
from rest_framework.views import APIView
from google.cloud import texttospeech

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
