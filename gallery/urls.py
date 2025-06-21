# gallery/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL for the main gallery page (e.g., http://127.0.0.1:8000/)
    path('', views.media_gallery, name='media_gallery'),
    # URL for the individual media item detail page
    path('item/<int:pk>/', views.media_detail, name='media_detail'),
    # URL for downloading media files
    path('download/<int:pk>/', views.download_media, name='download_media'),  # Add this line
]