import requests

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DataError, IntegrityError
from bestproduct.models import Product, UserFavorite

# More info : https://docs.djangoproject.com/fr/2.2/howto/custom-management-commands/

class Command(BaseCommand):
    help = 'delete all the entries in the database'

    def del_db(self):

        Product.objects.all().delete()

    def handle(self, *args, **options):
        self.del_db()
