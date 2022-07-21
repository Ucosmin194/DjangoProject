from django import forms
from django.forms import TextInput, Textarea, DateTimeInput, Select, BooleanField
from book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'format', 'category', 'summary', 'release_date', 'is_in_stock']

        widgets = {
            'title': TextInput(attrs={'placeholder': 'Please enter the book title', 'class': 'form-select'}),
            'author': TextInput(attrs={'placeholder': 'Please enter the books author', 'class': 'form-select'}),
            'format': Select(attrs={'class': 'form-select'}),
            'category': TextInput(attrs={'placeholder': 'Please enter the books category', 'class': 'form-select'}),
            'summary': Textarea(attrs={'placeholder': 'Please enter the books description', 'class': 'form-control'}),
            'release_date': DateTimeInput(attrs={'class': 'form-select', 'type': 'datetime-local'}),
    }
