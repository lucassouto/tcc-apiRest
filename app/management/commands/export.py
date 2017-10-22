import os.path

from django.core.management.base import BaseCommand
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from apiRest.utils.filescsv import create_one_register_csv, insert_one_register_csv
from app.models import Book
from app.serializers import BookSerializer



class Command(BaseCommand):
    help = 'Exports one/many records from the database'

    def __init__(self):
        super().__init__()
        self.book = ''


    def add_arguments(self, parser):
        parser.add_argument('id', nargs='+', type=int)

    def handle(self, *args, **options):
        for id_register in options['id']:
            try:
                self.book = Book.objects.get(pk=id_register)

                serializer = BookSerializer(self.book)
                json = JSONRenderer().render(serializer.data)
                stream = BytesIO(json)
                data = JSONParser().parse(stream)

                column_names = data.keys()
                if os.path.isfile('register.csv'):
                    insert_one_register_csv('register.csv', data, column_names)

                else:
                    create_one_register_csv('register.csv', data, column_names)

            except:
                if Book.DoesNotExist:
                    self.stdout.write('Register {} NotExist'.format(id_register))
                else:
                    self.stdout.write('Error Creating File')
