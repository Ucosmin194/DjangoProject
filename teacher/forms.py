from django import forms
from django.forms import TextInput, Textarea, DateTimeInput, Select
from teacher.models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-select'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-select'}),
            'department': Select(attrs={'placeholder': 'Please enter your department', 'class': 'form-select'}),
            'course': TextInput(attrs={'placeholder': 'Please enter your course name', 'class': 'form-select'}),
            'description': Textarea(attrs={'placeholder': 'Please enter your description', 'class': 'form-control'}),
            'start_date': DateTimeInput(attrs={'class': 'form-select', 'type': 'datetime-local'}),
            'end_date': DateTimeInput(attrs={'class': 'form-select', 'type': 'datetime-local'}),
            'campanii_auxiliare_active': TextInput(attrs={'placeholder': 'Please enter active campaigns',
                                                          'class': 'form-select'})
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        get_first_name = cleaned_data.get('first_name')
        get_last_name = cleaned_data.get('last_name')
        all_teachers = Teacher.objects.all()
        for teacher in all_teachers:
            if teacher.first_name == get_first_name and teacher.last_name == get_last_name:
                msg = 'Exista deja un profesor cu numele acesta'
                self._errors['first_name'] = self.error_class([msg])
        get_start_date = cleaned_data.get('start_date')
        get_end_date = cleaned_data.get('end_date')

        if get_start_date > get_end_date:
            msg = 'Wrong time, please try again'
            self._errors['start_date'] = self.error_class([msg])

        return cleaned_data
