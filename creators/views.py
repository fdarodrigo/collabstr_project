from django.shortcuts import render
from .models import Content

import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def content_list(request):
 
    """
    Fetches influencers' content, filtering by chosen platform
    if specified, else all, max 30 results.
    """

    platform = request.GET.get('platform', '')
    if platform:
        contents = Content.objects.select_related('creator').filter(creator__platform__iexact=platform)[:30]
    else:
        contents = Content.objects.select_related('creator').all()[:30]   
    return render(request, 'home.html', {'contents': contents})

@csrf_exempt
def download_file(request):

    """
    This view proxies file downloads from external URLs 
    to bypass CORS restrictions. It retrieves the file URL 
    and name from query parameters, 
    streaming the file content back with the correct content type and filename.
    """

    file_url = request.GET.get('url')
    file_name = request.GET.get('name')

    response = requests.get(file_url, stream=True)
    response.raise_for_status()

    content_type = response.headers['Content-Type']
    response = HttpResponse(response.raw, content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response