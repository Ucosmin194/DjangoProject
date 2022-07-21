import django_filters
from django import forms
from django_filters import DateTimeFilter

from book.models import Book


class BookFilter(django_filters.FilterSet):
    release_date_gte = DateTimeFilter(field_name='start_date', lookup_expr='gte', label='From release date',
                                      widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    release_date_lte = DateTimeFilter(field_name='start_date', lookup_expr='lte', label='To release date',
                                      widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))

    class Meta:
        model = Book
        fields = ['title', 'author', 'release_date_gte', 'release_date_lte', 'format', 'category', 'is_in_stock']

    def __init__(self, *args, **kwargs):
        super(BookFilter, self).__init__(*args, **kwargs)
        self.filters['title'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Search title'})
        self.filters['author'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Search author'})
        self.filters['format'].field.widget.attrs.update({'class': 'form-select'})
        self.filters['category'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Search category'}),

