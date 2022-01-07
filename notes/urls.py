from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'all-notes', views.NoteViewSet, basename='all')
router.register(r'my-notes', views.MyNoteViewSet, basename='my')

urlpatterns = router.urls