from django.urls import path
from . import views


urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('tracker/', views.tracker, name='tracker'),
    path('', views.index, name='index'),  # This will be the homepage
]
