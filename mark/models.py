from django.db import models

from student.models import Student
from teacher.models import Teacher


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark = models.IntegerField(null=True)
    assigned_by = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student.first_name} {self.student.last_name}'

