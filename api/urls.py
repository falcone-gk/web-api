from django.urls import include, path
from api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename="projects")

urlpatterns = [
    path('', include(router.urls)),
]