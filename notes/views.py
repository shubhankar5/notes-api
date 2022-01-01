from rest_framework import viewsets, permissions
from rest_framework.throttling import AnonRateThrottle
from .models import Note
from .serializers import NoteSerializer
from .throttlers import GetRateThrottle, PostRateThrottle


class NoteViewSet(viewsets.ModelViewSet):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	throttle_classes = [AnonRateThrottle]

	def get_throttles(self):
		if self.action in ['update', 'partial_update', 'destroy']:
			self.throttle_classes.append(PostRateThrottle)
		else:
			self.throttle_classes.append(GetRateThrottle)

		return super().get_throttles()