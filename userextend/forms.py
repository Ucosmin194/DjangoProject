from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, Textarea

from userextend.models import UserExtend


class UserExtendForm(UserCreationForm):
    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email', 'email_confirmation', 'username', 'age', 'gender', 'phone',
                  'mailing_address']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'email_confirmation': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email confirmation'}),
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your username'}),
            'age': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'gender': Select(attrs={'class': 'form-select', 'placeholder': 'Please select your gender'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your phone number'}),
            'mailing_address': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your mailing address'})

        }

    def __init__(self, *args, **kwargs):
        super(UserExtendForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Please enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Please enter your password confirmation'
