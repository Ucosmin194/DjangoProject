import django_filters
from django import forms
from django_filters import DateTimeFilter, CharFilter

from teacher.models import Teacher


class TeacherFilter(django_filters.FilterSet):
    start_date_gte = DateTimeFilter(field_name='start_date', lookup_expr='gte', label='From start date',
                                    widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    start_date_lte = DateTimeFilter(field_name='start_date', lookup_expr='lte', label='To start date',
                                    widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    end_date_gte = DateTimeFilter(field_name='end_date', lookup_expr='gte', label='From end date',
                                  widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    end_date_lte = DateTimeFilter(field_name='end_date', lookup_expr='lte', label='To end date',
                                  widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    first_name_istartswith = CharFilter(field_name='first_name', lookup_expr='istartswith', label='First name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}))

    class Meta:
        model = Teacher
        fields = ['first_name_istartswith', 'last_name', 'start_date_gte', 'start_date_lte', 'end_date_gte', 'end_date_lte', 'course', 'department']

    def __init__(self, *args, **kwargs):
        super(TeacherFilter, self).__init__(*args, **kwargs)

        self.filters['last_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Search last name'})
        self.filters['course'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Search course'})
        self.filters['department'].field.widget.attrs.update(
            {'class': 'form-select'})