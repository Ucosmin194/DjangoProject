from django.db import models

from teacher.models import Teacher


class Student(models.Model):
    gender_options = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_olympic = models.BooleanField(default=False)
    gender = models.CharField(max_length=6, choices=gender_options)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

