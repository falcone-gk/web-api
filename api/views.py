from api.models import Project, Post, Tag
from api.serializers import ProjectSerializer, GetProjectSerializer, PostSummarySerializer, PostSerializer, TagSerializer

from rest_framework import status, viewsets, mixins, views, generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

# Create your views here.

class ListTagAPIView(views.APIView):

    def get(self, request, format=None):

        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API to show the projects that I made. In this case the only person who can
    create and edit a Project summary is an Admin.
    """

    queryset = Project.objects.all()

    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):

        if self.action == 'list' or self.action == 'retrieve':
            return GetProjectSerializer
        else:
            return ProjectSerializer

class ListPostSummary(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    API to send post's summary (title, description and date created). It is sent
    with pagination so that the posts are sent in parts.
    """

    queryset = Post.objects.all()
    serializer_class = PostSummarySerializer
    permission_classes = [AllowAny,]

class RetrieveCreateUpdateDeletePost(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin):

    """
    API that get, create, edit and delete a post. The las three can do it just
    an admin.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):

        if self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

class HomeAPIView(views.APIView):
    """
    API that send data to home page in frontend.
    It's sent some projects and posts.
    """

    def get(self, request, format=None):

        projects = Project.objects.all().order_by('-id')[:8]
        posts = Post.objects.all().order_by('-id')[:8]

        serializer_project = GetProjectSerializer(projects, many=True)
        serializer_post = PostSummarySerializer(posts, many=True)

        json_data = {
            'summary_project': serializer_project.data,
            'summary_post': serializer_post.data
        }

        return Response(json_data, status=status.HTTP_200_OK)