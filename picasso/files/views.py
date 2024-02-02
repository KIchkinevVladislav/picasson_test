from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import filters

from .models import File
from .serializers import FileSerializer


class FileListView(ListAPIView):
    """
    Returns a list of all objects File.    
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
   
    filterset_fields = ['processed']
    search_fields = ['uploaded_at']
    ordering_fields = ['uploaded_at']


class CreateFileView(CreateAPIView):
    """
    View for creating a new object File.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer