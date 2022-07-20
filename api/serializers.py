from enum import unique
from rest_framework import serializers
from api.models import Project, Post, Tag

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

class GetProjectSerializer(serializers.ModelSerializer):
    """
    Serializing the entire Project model. This serializer will be used to just show
    when user do a get request.
    """

    tags = TagSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializing the entire Project model. This serializer is used when an admin
    wants to create, update or delete a Project.
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