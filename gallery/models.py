from django.db import models
import os

# Create your models here.

# gallery/models.py

class MediaItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # The 'upload_to' argument specifies a subdirectory of MEDIA_ROOT
    # to store the files.
    file = models.FileField(upload_to='media_files/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def file_type(self):
        name, extension = os.path.splitext(self.file.name)
        if extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
            return 'image'
        elif extension.lower() in ['.mp4', '.mov', '.avi', '.webm']:
            return 'video'
        else:
            return 'other'

    class Meta:
        ordering = ['-upload_date']
        verbose_name = "Media Item"
        verbose_name_plural = "Media Items"