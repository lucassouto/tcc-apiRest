import os.path
from django.core.management.base import BaseCommand
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from apiRest.utils.filescsv import create_many_register_csv, insert_many_register_csv
from app.models import Book
from app.serializers import BookSerializer


class Command(BaseCommand):
    help = 'Exports all records from the database'

    def __init__(self):
        super().__init__()
        self.book = ''


    def handle(self, *args, **options):
        try:
            self.book = Book.objects.all()

            serializer = BookSerializer(self.book, many=True)

            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)

            columns_names = data[0].keys()

            if os.path.isfile('register.csv'):
                insert_many_register_csv('register.csv', data, columns_names)

            else:
                create_many_register_csv('register.csv', data, columns_names)

            self.stdout.write('Saved')

        except Book.DoesNotExist:
            self.stdout.write('Records NotExist')
