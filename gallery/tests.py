from django.test import TestCase
from .models import MediaItem
from django.core.files.uploadedfile import SimpleUploadedFile

class MediaItemModelTest(TestCase):
    def test_create_image_item(self):
        file = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
        item = MediaItem.objects.create(title="Test Image", file=file)
        self.assertEqual(item.file_type, 'image')
