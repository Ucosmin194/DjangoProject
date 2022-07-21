from django.urls import path

from intro import views

urlpatterns = [
    path('intro/', views.show_name, name='hello'),
    path('all-students/', views.students, name='all_students'),
    path('all-movies/', views.all_awesome_movies, name='all_movies')
]

