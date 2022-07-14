from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Photos
from .serializer import PhotoSerializer
from rest_framework.decorators import action

class PhotoView(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photos.objects.all()


    @action(detail=True, methods=['post'])
    def add_photo(request):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete_photo(request, pk):
        photo = Photos.objects.get(id=pk)
        photo.delete()


