from django.shortcuts import render, redirect
from mainapp.models import TODO
# Create your views here.

def home(request):
    todos = TODO.objects.all()

    context = {'todos':todos}

    return render(request, 'home.html', context)

def add(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    else:
        title = request.POST['title']
        desc = request.POST['desc']

        TODO.objects.create(title = title, desc = desc)

        return redirect('home')    

def edit(request, id):
    todo = TODO.objects.get(id=id)
    if request.method == 'GET':
        context = {'todo':todo}
        return render(request, 'edit.html', context)
    else:
        todo.title = request.POST['title']
        todo.desc = request.POST['desc']

        todo.save()
        return redirect('home')
    

def delete(request, id):
    todo = TODO.objects.get(id = id)
    todo.delete()
    return redirect('home')

def delete_all(request):
    TODO.objects.all().delete()
    return redirect('home')

def mark_as_complete(request, id):
    todo = TODO.objects.get(id = id)

    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('home')
