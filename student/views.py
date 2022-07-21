from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from student.filters import StudentFilter
from student.forms import StudentForm
from student.models import Student
from teacher.models import Teacher


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'student/create_student.html'  #calea catre fisierul html
    model = Student
    # fields = '__all__'
    form_class = StudentForm
    success_url = reverse_lazy('create_new_student')
    permission_required = 'student.add_student'


class StudentListView(LoginRequiredMixin, ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'

    def get_queryset(self):
        return Student.objects.filter(active=True)

    def get_context_data(self,  **kwargs):
        data = super(StudentListView, self).get_context_data()
        # all_teachers = Teacher.objects.all()
        # data['teachers'] = all_teachers
        students = Student.objects.all()
        myFilter = StudentFilter(self.request.GET, queryset=students)
        data['all_students'] = myFilter.qs
        data['myFilter'] = myFilter

        return data


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list_of_students')
    permission_required = 'student.change_student'


class StudentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'student/details_student.html'
    model = Student


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list_of_students')
    permission_required = 'student.delete_student'


@login_required
def inactive_student(request, pk):
    Student.objects.filter(id=pk).update(active=False)
    return redirect('list_of_students')
