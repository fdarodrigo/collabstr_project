from django.shortcuts import render
from .models import Content


def content_list(request):
    """
    Escrever aqui o que a view faz
    """
    contents = Content.objects.select_related('creator').all()[:30]
    
    return render(request, 'home.html', {'contents': contents})

