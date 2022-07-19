from rest_framework import serializers
from api.models import Project, Post

class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializing the entire Project model.
    """

    class Meta:
        model = Project
        fields = '__all__'

class ResumePostSerializer(serializers.ModelSerializer):
    """
    Serializing just some fields from Post serializer because this is used
    when we want to show just a post summary.
    """

    class Meta:
        model = Post
        fields = ('title', 'description', 'created')