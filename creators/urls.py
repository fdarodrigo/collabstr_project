from django.urls import path
from .views import content_list, download_file

urlpatterns = [
    path('', content_list, name='content_list'),
    path('download/', download_file, name='download_file'),
]
