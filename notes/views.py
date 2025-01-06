# from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

# from .serializers import UploadSerializer
from .models import Note
from .serializers import NoteSerializer


class NoteList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # queryset = Note.objects.all()
    # serializer_class = NoteSerializer


class NoteDetail(APIView):
    permission_classes = [IsAuthenticated]

    # def detail(self, request, pk):
    #     try:
    #         note = Note.objects.get(pk=pk, user=request.user)
    #     except Note.DoesNotExist:
    #         raise Http404
    #     return note

    def get(self, request, pk):
        # note = self.detail(pk=pk)
        note = Note.objects.get(pk=pk, user=request.user)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def put(self, request, pk):
        # note = self.detail(pk=pk)
        note = Note.objects.get(pk=pk, user=request.user)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # note = self.detail(pk=pk)
        note = Note.objects.get(pk=pk, user=request.user)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class UploadViewSet(ViewSet):
#     serializer_class = UploadSerializer
#
#     def list(self, request):
#         return Response("GET API")
#
#     def create(self, request):
#         file_uploaded = request.FILES.get('file_uploaded')
#         content_type = file_uploaded.content_type
#         response = "POST API and you have uploaded a {} file".format(content_type)
#         return Response(response)