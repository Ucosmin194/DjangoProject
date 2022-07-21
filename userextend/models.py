from django.contrib.auth.models import User
from django.db import models


class UserExtend(User):
    gender_options = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))

    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=gender_options)
    email_confirmation = models.EmailField(max_length=100)
    phone = models.IntegerField()
    mailing_address = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
