import django_filters
from django import forms
from django_filters import DateTimeFilter

from student.models import Student


class StudentFilter(django_filters.FilterSet):
    start_date_gte = DateTimeFilter(field_name='start_date', lookup_expr='gte', label='From start date',
                                    widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    start_date_lte = DateTimeFilter(field_name='start_date', lookup_expr='lte', label='To start date',
                                    widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))

    end_date_gte = DateTimeFilter(field_name='end_date', lookup_expr='gte', label='From end date',
                                  widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    end_date_lte = DateTimeFilter(field_name='end_date', lookup_expr='lte', label='To end date',
                                  widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'start_date_gte', 'start_date_lte', 'end_date_gte', 'end_date_lte',
                  'gender', 'email']

    def __init__(self, *args, **kwargs):
        super(StudentFilter, self).__init__(*args, **kwargs)
        self.filters['first_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Search first name'})
        self.filters['last_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Search last name'})
        self.filters['email'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Search email'})
        self.filters['gender'].field.widget.attrs.update({'class': 'form-select'})
