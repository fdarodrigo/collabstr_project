from django.urls import path
from .views import content_list

urlpatterns = [
    path('', content_list, name='content_list'),
]
