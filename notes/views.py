from rest_framework import viewsets, permissions, filters
from rest_framework.throttling import AnonRateThrottle
from django_filters import rest_framework as django_filters
from .models import Note
from .serializers import NoteSerializer
from .throttlers import GetRateThrottle, PostRateThrottle
from .paginators import NoteResultsSetPagination
from .filters import NoteFilter


class NoteViewSet(viewsets.ModelViewSet):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
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