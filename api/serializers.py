from pyexpat import model
from rest_framework import serializers
from api.models import Project, Post

class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializing the entire Project model.
    """

    class Meta:
        model = Project
        fields = '__all__'

class PostSummarySerializer(serializers.ModelSerializer):
    """
    Serializing just some fields from Post serializer because this is used
    when we want to show just a post summary.
    """

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'created')

class PostSerializer(serializers.ModelSerializer):
    """
    Serializing the entire Post model. This is used to show a post.
    """

    class Meta:
        model = Post
        fields = '__all__'