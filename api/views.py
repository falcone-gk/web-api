from api.models import Project, Post
from api.serializers import ProjectSerializer, ResumePostSerializer

from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):

        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = ResumePostSerializer