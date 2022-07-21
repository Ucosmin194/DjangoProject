from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from student.models import Student
from teacher.filters import TeacherFilter
from teacher.forms import TeacherForm
from teacher.models import Teacher


class TeacherCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'teacher/create_teacher.html'
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('create_new_teacher')
    permission_required = 'teacher.add_teacher'


class TeacherListView(LoginRequiredMixin, ListView):
    template_name = 'teacher/list_of_teachers.html'
    model = Teacher
    context_object_name = 'all_teachers'

    def get_queryset(self):
        return Teacher.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        data = super(TeacherListView, self).get_context_data()
        teachers = Teacher.objects.all()
        myFilter = TeacherFilter(self.request.GET, queryset=teachers)
        data['all_teachers'] = myFilter.qs
        data['myFilter'] = myFilter

        return data


class TeacherUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'teacher/update_teacher.html'
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('list_of_teachers')
    permission_required = 'teacher.change_teacher'


class TeacherDetailView(LoginRequiredMixin, DetailView):
    template_name = 'teacher/details_teacher.html'
    model = Teacher


class TeacherDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'teacher/delete_teacher.html'
    model = Teacher
    success_url = reverse_lazy('list_of_teachers')
    permission_required = 'teacher.delete_teacher'


@login_required
def inactive_teacher(request, pk):
    Teacher.objects.filter(id=pk).update(active=False)
    return redirect('teacher.list_of_teachers')


def get_all_students_per_teacher(reqeust, pk):
    all_students_per_teacher = Student.objects.filter(teacher_id=pk)
    context = {'all_students_per_teacher': all_students_per_teacher}
    return render(reqeust, 'teacher/all_students_per_teacher.html', context)
