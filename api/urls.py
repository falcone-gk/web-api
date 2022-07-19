from django.urls import include, path
from api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename="projects")
router.register(r'posts-summary', views.ListPostSummary, basename="posts-summary")
router.register(r'posts', views.RetrieveCreateUpdateDeletePost, basename="posts")

urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.HomeAPIView.as_view(), name='api-home'),
]