from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework import filters

from .models import File
from .serializers import FileSerializer


class FileListView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
   
    filterset_fields = ['processed']
    search_fields = ['uploaded_at']
    ordering_fields = ['uploaded_at']