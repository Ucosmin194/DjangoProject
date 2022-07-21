from django.db import models


class Teacher(models.Model):
    select_options = (('p', 'Python'), ('j', 'Java'), ('c', 'C#'))

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=6, choices=select_options)
    course = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    campanii_auxiliare_active = models.CharField(max_length=100)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
