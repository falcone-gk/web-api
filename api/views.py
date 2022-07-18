from api.models import Project
from api.serializers import ProjectSerializer

from rest_framework import status, viewsets, mixins
from rest_framework.response import Response

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer