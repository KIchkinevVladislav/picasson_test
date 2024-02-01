from django.urls import path

from .views import FileListView

app_name = 'files'


urlpatterns = [
    path('files/', FileListView.as_view(), name='list_files'),
]