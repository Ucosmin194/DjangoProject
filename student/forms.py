from django import forms
from django.forms import TextInput, EmailInput, Textarea, DateTimeInput, Select
from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'age', 'description',
                  'start_date', 'end_date', 'is_olympic', 'gender', 'teacher']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-select'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-select'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-select'}),
            'age': TextInput(attrs={'placeholder': 'Please enter your age', 'class': 'form-select'}),
            'description': Textarea(attrs={'placeholder': 'Please enter your description', 'class': 'form-control'}),
            'start_date': DateTimeInput(attrs={'class': 'form-select', 'type': 'datetime-local'}),
            'end_date': DateTimeInput(attrs={'class': 'form-select', 'type': 'datetime-local'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'teacher': Select(attrs={'class': 'form-select'})
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        get_age = cleaned_data.get('age')

        if get_age < 18:
            msg = 'Studentul nu poate fi minor'
            self._errors['age'] = self.error_class([msg])
            
        return cleaned_data

