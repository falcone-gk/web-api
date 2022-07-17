from django.urls import include, path
from projects import views

urlpatterns = [
    path('posts/', views.ListPost.as_view(), name='posts-list'),
]