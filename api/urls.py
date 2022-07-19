from django.urls import include, path
from api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename="projects")
router.register(r'posts-summary', views.ListRetrievePostSummary, basename="posts-summary")

urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.HomeAPIView.as_view(), name='api-home'),
]