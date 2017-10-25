from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO

from app.models import Book

class CommandExportTest(TestCase):
    def test_command_export(self):
        Book.objects.create()
        out = StringIO()
        call_command('export', 1, stdout=out)
        self.assertIn('Saved', out.getvalue())

    def test_command_exportall(self):
        Book.objects.create()
        out = StringIO()
        call_command('exportall', stdout=out)
        self.assertIn('Saved', out.getvalue())
