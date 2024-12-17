from django.urls import path
from . import views
# from .views import Signup

urlpatterns = [
    path('', views.Signup, name='Signup'),
    path('Signin/', views.Signin, name='Signin'),
    path('Home/', views.Home, name='Home'),
    path('filter/', views.filter_teachers, name='filter_teachers'),
    path('rating/', views.teacher_list, name='teacher_list'),
]

    