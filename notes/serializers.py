from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password', 'is_staff']


class NoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		fields = '__all__'