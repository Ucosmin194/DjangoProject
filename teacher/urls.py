from django.urls import path
from teacher import views

urlpatterns = [
    path('create-new-teacher/', views.TeacherCreateView.as_view(), name='create_new_teacher'),
    path('list-of-teachers/', views.TeacherListView.as_view(), name='list_of_teachers'),
    path('update-teacher/<int:pk>/', views.TeacherUpdateView.as_view(), name='update_teacher'),
    path('details-teacher/<int:pk>/', views.TeacherDetailView.as_view(), name='details_teacher'),
    path('delete-teacher/<int:pk>/', views.TeacherDeleteView.as_view(), name='delete_teacher'),
    path('inactive-teacher/<int:pk>/', views.inactive_teacher, name='inactive_teacher'),
    path('all-students-per-teacher/<int:pk>/', views.get_all_students_per_teacher, name='all_students_per_teacher')
]
