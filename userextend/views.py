from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from djangoProjectSDA.settings import EMAIL_HOST_USER
from userextend.forms import UserExtendForm


class UserextendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserExtendForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            create_user = form.save(commit=False)
            create_user.username = form.cleaned_data['username'].upper()

            create_user.save()
            message = f'Hello {create_user.first_name} {create_user.last_name} \n Welcome to my app! \n Your username is: {create_user.username}'
            send_mail('Create a new user', message, from_email=EMAIL_HOST_USER, recipient_list=[create_user.email])

        return redirect('login')
