from rest_framework import serializers

from .models import Note
from rest_framework.serializers import Serializer, FileField

# Serializers define the API representation.


# class UploadSerializer(Serializer):
#     file_uploaded = FileField()
#
#     class Meta:
#         fields = ['Note File']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'text', 'is_done', 'is_public', 'updated_time']
        extra_kwargs = {
            'user': {'read_only': True}
        }