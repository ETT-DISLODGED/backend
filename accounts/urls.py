from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('update/', UserUpdateView.as_view()),
    path('password/', PasswordUpdateView.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # username&password -> accesss
    path('refresh/token/', TokenRefreshView.as_view(), name='token_refresh'), # refresh -> access

    path('mypost/', MyPostView.as_view()),

    path('myvoice/',VoiceInfoView.as_view()),

]