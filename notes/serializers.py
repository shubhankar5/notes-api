from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'id', 'username', 'first_name', 'last_name', 'email', 'password', 'is_staff']

	def create(self, validated_data):
		password = validated_data.pop('password', None)
		instance = self.Meta.model(**validated_data)
		if password is not None:
		    instance.set_password(password)
		instance.save()
		return instance

	def update(self, instance, validated_data):
		for attr, value in validated_data.items():
			if attr == 'password':
				instance.set_password(value)
			else:
				setattr(instance, attr, value)
		instance.save()
		return instance


class NoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		fields = '__all__'


class NoteHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(
		view_name='all-note-detail',
	)
	owner = serializers.HyperlinkedRelatedField(
		view_name = 'user-detail',
		queryset = User.objects.all(),
	)

	class Meta:
		model = Note
		fields = ['url', 'id', 'title', 'text', 'owner', 'created_on']


class MyNoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		exclude = ['owner']