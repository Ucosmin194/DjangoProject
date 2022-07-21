from django.db import models


class Book(models.Model):
    format_options = (('kindle', 'Kindle'), ('paperback', 'Paperback'), ('audiobook', 'Audiobook'))

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    format = models.CharField(max_length=9, choices=format_options)
    category = models.CharField(max_length=30)
    summary = models.TextField()
    release_date = models.DateTimeField()
    is_in_stock = models.BooleanField()

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.author}'
