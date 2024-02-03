import pytest

from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from files.models import File
from files.serializers import FileSerializer


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass

@pytest.mark.django_db
def test_file_list_view(api_client):
    # Checking the receipt of a list of files
    url = reverse('files:list_files')
    response = api_client.get(url)
    assert response.status_code == 200
    assert 'results' in response.json()

    # Filtering check
    response_filtered = api_client.get(url, {'processed': True})
    assert response_filtered.status_code == 200
    assert all(file['processed'] for file in response_filtered.json()['results'])

    # Check search
    response_search = api_client.get(url, {'search': 'your_search_query'})
    assert response_search.status_code == 200
    assert all('your_search_query' in file['uploaded_at'] for file in response_search.json()['results'])

    # Check sorting
    response_sorted = api_client.get(url, {'ordering': '-uploaded_at'})
    assert response_sorted.status_code == 200
    assert all(response_sorted.json()['results'][i]['uploaded_at'] >= response_sorted.json()['results'][i+1]['uploaded_at']
               for i in range(len(response_sorted.json()['results']) - 1))


@pytest.mark.django_db
def test_create_file_invalid_data(api_client):
    invalid_file_data = {
        # Required field "file" is missing
    }

    url = reverse('files:create_file')
    response = api_client.post(url, data=invalid_file_data, format='json')

    assert response.status_code == HTTP_400_BAD_REQUEST

    assert File.objects.count() == 0