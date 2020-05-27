from rest_framework import serializers
from .models import MC_Question, Choice, Profile, Attempt
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MC_QuestionSerializer(serializers.HyperlinkedModelSerializer):
    related_choices = serializers.StringRelatedField(many=True)
    class Meta:
        model = MC_Question
        fields = ['id', 'url', 'question', 'related_choices']

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__' 

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    related_user = serializers.StringRelatedField(many=True)
    class Meta:
        model = Profile
        fields = ['related_user', 'url', 'score']

class AttemptSerializer(serializers.HyperlinkedModelSerializer):
    # related_user = serializers.StringRelatedField(many=True)
    class Meta:
        model = Attempt
        fields = '__all__'
