import datetime

from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.
from django.utils import timezone


class File(models.Model):
    file = models.FileField(upload_to="media/")
    created_at = models.DateTimeField(default=timezone.now)
