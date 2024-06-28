import json
import os
import django
from creators.models import Creator, Content

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collabstr_project.settings')
django.setup()


def populate():
    with open('creators.json') as file:
        data = json.load(file)
        for creator_data in data:
            creator = Creator(
                name=creator_data['name'],
                username=creator_data['username'],
                rating=creator_data['rating'],
                platform=creator_data['platform']
            )
            creator.save()
            content = Content(
                creator=creator,
                url=creator_data['content']
            )
            content.save()

if __name__ == '__main__':
    populate()
