from api.models import Project, Post
from api.serializers import ProjectSerializer, ResumePostSerializer

from rest_framework import status, viewsets, mixins, views
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

class ListRetrievePost(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):

    queryset = Post.objects.all()
    serializer_class = ResumePostSerializer
    permission_classes = [AllowAny,]

class HomeAPIView(views.APIView):

    def get(self, request, format=None):

        projects = Project.objects.all().order_by('-id')[:8]
        posts = Post.objects.all().order_by('-id')[:8]

        serializer_project = ProjectSerializer(projects, many=True)
        serializer_post = ResumePostSerializer(posts, many=True)

        json_data = {
            'summary_project': serializer_project.data,
            'summary_post': serializer_post.data
        }

        return Response(json_data, status=status.HTTP_200_OK)