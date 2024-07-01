from django.urls import path
from .views import content_list, filtered_content_list, download_file

urlpatterns = [
    path('', content_list, name='content_list'),
    path('filtered/', filtered_content_list, name='filtered_content_list'),
    path('download/', download_file, name='download_file'),
]
