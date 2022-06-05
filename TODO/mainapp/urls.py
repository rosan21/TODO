from django.urls import path
from mainapp import views

urlpatterns = [
    path('home/' , views.home, name = 'home'),
    path('', views.home),
    path('add/', views.add, name = 'add'),
    path('edit/<int:id>', views.edit, name = 'edit')
]