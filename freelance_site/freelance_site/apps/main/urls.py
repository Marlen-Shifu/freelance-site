from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.user_login),
    path('lesson1/', views.view_lesson1),
    path('lesson2/', views.view_lesson2),
    path('lesson3/', views.view_lesson3),
]