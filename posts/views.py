from .serializers import *
from .permissions import AuthenticatedOnly
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets, filters

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    # filter_backends = [filters.SearchFilter] 검색 기능 미정
    # search_fields = ['content', 'user__nickname']

    permission_classes = [IsAuthenticated, AuthenticatedOnly]


    def perform_create(self, serializer):
        serializer.save(author = self.request.user)