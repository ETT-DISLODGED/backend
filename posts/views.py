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