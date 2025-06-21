# Create your views here.
# gallery/views.py
from django.shortcuts import render, get_object_or_404
from .models import MediaItem
from django.http import FileResponse, Http404
import os

def media_gallery(request):
    # Get all media items, ordered by the newest first
    items = MediaItem.objects.all().order_by('-upload_date')
    context = {
        'items': items
    }
    return render(request, 'gallery/media_gallery.html', context)

def media_detail(request, pk):
    # Get the specific media item or return a 404 error if not found
    item = get_object_or_404(MediaItem, pk=pk)
    context = {
        'item': item
    }
    return render(request, 'gallery/media_detail.html', context)

def download_media(request, pk):
    item = get_object_or_404(MediaItem, pk=pk)
    file_path = item.file.path
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
        return response
    else:
        raise Http404("File does not exist")