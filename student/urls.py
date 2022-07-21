from django.urls import path
from student import views

urlpatterns = [
    path('create-new-student/', views.StudentCreateView.as_view(), name='create_new_student'),
    path('list-of-students/', views.StudentListView.as_view(), name='list_of_students'),
    path('update-student/<int:pk>/', views.StudentUpdateView.as_view(), name='update_student'),
    path('details-student/<int:pk>/', views.StudentDetailView.as_view(), name='details_student'),
    path('delete-student/<int:pk>/', views.StudentDeleteView.as_view(), name='delete_student'),
    path('inactive-student/<int:pk>/', views.inactive_student, name='inactive_student')
]
