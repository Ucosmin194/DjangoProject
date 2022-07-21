from django.urls import path
from userextend import views

urlpatterns = [
    path('create-user', views.UserextendCreateView.as_view(), name='create_user'),

]