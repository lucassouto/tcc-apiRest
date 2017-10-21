from django.db import models

LANGUAGE_CHOICES = (
    ('pt-br', 'Portugues Brasil'),
    ('en', 'Inglês')
)

class Book(models.Model):
    title = models.CharField(max_length=50, null=True)
    author = models.CharField(max_length=75, null=True)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, null=True)
    release_date = models.DateField(null=True)

    class Meta:
        ordering = ('release_date',)
        