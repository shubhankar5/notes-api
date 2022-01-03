import django_filters
from .models import Note


class NoteFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        fields = {
            'title': ['iexact'],
            'text': ['icontains'],
            'owner__username': ['iexact'],
            'created_on': ['lte', 'gte', 'range']
        }