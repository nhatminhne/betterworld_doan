from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from backend.models import Projects, Users, Contribution

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'creatorId', 'name', 'category', 'description', 'image', 'imageName', 'targetPrice', 'isFeatured', 'currentPrice', 'donationCount', 'createAt')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'email', 'avatar', 'coverBackground', 'description', 'facebook', 'phone', 'createAt')

class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = ('id', 'userId', 'projectId', 'amount', 'createAt')
