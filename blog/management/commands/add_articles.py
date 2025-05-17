from django.core.management.base import BaseCommand
from blog.models import Article
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        Article.objects.all().delete()

        call_command('loaddata', 'articles_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
