"""
    Cria um arquivo .csv com base nos argumentos passados para o comando.
"""
import csv
from django.core.management.base import BaseCommand
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from app.models import Book
from app.serializers import BookSerializer


class Command(BaseCommand):
    help = 'Exporta todos os registros do banco de dados'

    def __init__(self):
        super().__init__()
        self.book = ''


    def add_arguments(self, parser):
        parser.add_argument('id', nargs='+')

    def handle(self, *args, **options):
        for id_register in options['id']:
            try:
                self.book = Book.objects.get(pk=id_register)

                serializer = BookSerializer(self.book)
                json = JSONRenderer().render(serializer.data)
                stream = BytesIO(json)
                data = JSONParser().parse(stream)
                
                with open('register.csv', 'a') as arq:
                    fieldnames = ['release_date', 'language', 'title', 'author', 'id']
                    csv.DictWriter(arq, fieldnames=fieldnames).writerow(data)

            except:
                if Book.DoesNotExist:
                    self.stdout.write('Register {} NotExist'.format(id_register))
                else:
                    self.stdout.write('Error Creating File')

