from rest_framework import serializers
from api.models import Project, Post

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

class ResumePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'description', 'created')