from django.urls import path
from mainapp import views

urlpatterns = [
    path('home/' , views.home, name = 'home'),
    path('', views.home)
]