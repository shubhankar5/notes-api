from rest_framework import viewsets, permissions, filters, versioning
from rest_framework.throttling import AnonRateThrottle
from django_filters import rest_framework as django_filters
from django.contrib.auth.models import User
from .models import Note
from .serializers import UserSerializer, NoteSerializer, MyNoteSerializer, NoteHyperlinkedSerializer
from .throttlers import GetRateThrottle, PostRateThrottle
from .paginators import UserResultsSetPagination, NoteResultsSetPagination
from .filters import NoteFilter


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAdminUser]
	throttle_classes = [AnonRateThrottle]
	pagination_class = UserResultsSetPagination
	filter_backends = [filters.SearchFilter, filters.OrderingFilter]
	search_fields = ['$username']
	ordering_fields = ['username']

	def get_throttles(self):
		if self.action in ['update', 'partial_update', 'destroy']:
			self.throttle_classes.append(PostRateThrottle)
		else:
			self.throttle_classes.append(GetRateThrottle)

		return super().get_throttles()


class BaseNoteViewSet(viewsets.ModelViewSet):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer
	permission_classes = [permissions.IsAdminUser]
	throttle_classes = [AnonRateThrottle]
	pagination_class = NoteResultsSetPagination
	filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	filterset_class = NoteFilter
	search_fields = ['$title', '=owner__username']
	ordering_fields = ['title', 'owner__username', 'created_on']

	def get_throttles(self):
		if self.action in ['update', 'partial_update', 'destroy']:
			self.throttle_classes.append(PostRateThrottle)
		else:
			self.throttle_classes.append(GetRateThrottle)

		return super().get_throttles()


class NoteViewSet(BaseNoteViewSet):
	versioning_class = versioning.QueryParameterVersioning

	def get_serializer_class(self):
	    if self.request.version == '0.1':
	        return NoteHyperlinkedSerializer
	    return NoteSerializer


class MyNoteViewSet(BaseNoteViewSet):
	serializer_class = MyNoteSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
	    return self.request.user.notes.all()

	def perform_create(self, serializer):
		serializer.save(owner = self.request.user)

	def perform_update(self, serializer):
		serializer.save(owner = self.request.user)
