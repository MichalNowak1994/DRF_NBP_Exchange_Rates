from django.core.management import BaseCommand

from nbp.models import ExchangeRate


class Command(BaseCommand):
    help = 'Clear the database by deleting all objects'

    def add_arguments(self, parser):
        parser.add_argument('--confirm', action='store_true',
                            help='Confirm before deleting all objects')

    def handle(self, *args, **options):
        if options['confirm']:
            confirm = input('Are you sure you want to delete all objects? (y/n): ')
            if confirm != 'y':
                return "Aborting."
        if ExchangeRate.objects.exists():
            ExchangeRate.objects.all().delete()
            return "All objects deleted"
        else:
            return "There are no object to delete"
