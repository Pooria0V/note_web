from django.db import models
from django.conf import settings


class Note(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    # image = models.ImageField(blank=True)
    is_public = models.BooleanField(default=True)
    is_done = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'


class NoteFile(models.Model):
    note = models.ForeignKey(to=Note, on_delete=models.CASCADE)
    # image = models.ImageField(blank=True)
    file = models.FileField(blank=True, null=True)

    class Meta:
        verbose_name = 'Note File'
        verbose_name_plural = 'Notes File'