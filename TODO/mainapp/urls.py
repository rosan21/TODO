from django.urls import path
from mainapp import views

urlpatterns = [
    path('home/' , views.home, name = 'home'),
    path('', views.home),
    path('add/', views.add, name = 'add'),
    path('edit/<int:id>', views.edit, name = 'edit'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('delete-all/', views.delete_all, name = 'delete-all'),
    path('mark-as-complete/<int:id>', views.mark_as_complete, name = 'mark-as-complete'),
    path('test/', views.test, name = 'test')
]