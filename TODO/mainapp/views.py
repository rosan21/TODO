from django.shortcuts import render
from mainapp.models import TODO
# Create your views here.

def home(request):
    todos = TODO.objects.all()

    context = {'todos':todos}

    return render(request, 'home.html', context)

def add(request):
    return render(request, 'add.html')

def edit(request, id):
    todo = TODO.objects.get(id=id)
    context = {'todo':todo}
    return render(request, 'edit.html', context)