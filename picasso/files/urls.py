from django.urls import path

from .views import FileListView, CreateFileView

app_name = 'files'


urlpatterns = [
    path('files/', FileListView.as_view(), name='list_files'),
    path('upload/', CreateFileView.as_view(), name='create_file'),
]