from django.db import models

class Creator(models.Model):
    """
    Escrever aqui o que o modelo faz
    """
    PLATFORMS = [
        ('Instagram', 'Instagram'),
        ('TikTok', 'TikTok'),
        ('User Generated Content', 'User Generated Content'),
    ]
    name = models.CharField(max_length=100) #colocar se é null e blank, se é default
    username = models.CharField(max_length=100)
    rating = models.FloatField() #passa parâmetro default
    platform = models.CharField(max_length=25, choices=PLATFORMS)

    def __str__(self):
        return self.name

class Content(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.url
