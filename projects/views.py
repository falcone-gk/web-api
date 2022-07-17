from projects.models import Project
from projects.serializers import ProjectSerializer

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class ListPost(generics.ListAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    page_size = 1