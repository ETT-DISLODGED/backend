from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'posts'
router = DefaultRouter()

router.register('post', PostViewSet) #comment list볼러면 설정해줘야함..
router.register('comment',CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tts/', TextToSpeechAPIView.as_view(), name='text_to_speech'),

]