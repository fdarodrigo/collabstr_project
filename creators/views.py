from django.shortcuts import render
from .models import Content

import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def content_list(request):
    platform = request.GET.get('platform', '')
    if platform:
        contents = Content.objects.select_related('creator').filter(creator__platform__iexact=platform)
    else:
        contents = Content.objects.select_related('creator').all()[:30]
    return render(request, 'home.html', {'contents': contents})

def filtered_content_list(request):
    platform = request.GET.get('platform', '')
    if platform:
        contents = Content.objects.select_related('creator').filter(creator__platform__iexact=platform)[:30]
    else:
        contents = Content.objects.select_related('creator').all()[:30]
    
    return render(request, 'home.html', {'contents': contents})

@csrf_exempt
def download_file(request):
    file_url = request.GET.get('url')
    file_name = request.GET.get('name')

    response = requests.get(file_url, stream=True)
    response.raise_for_status()

    content_type = response.headers['Content-Type']
    response = HttpResponse(response.raw, content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    
    return response