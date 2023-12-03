from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Todo
from django.contrib import messages
from .form import TodoCreateForm, TodoUpdateForm

# Create your views here.

# def say_hello(request):
#     return HttpResponse('hello user...')

# def say_hello(request):
#     return render(request, 'hello.html', {'name': 'admin', 'last_name': 'gilani'})

def home(request):
    all = Todo.objects.all()
    var2= Todo.objects.filter(title='Seven')
    return render(request, 'home.html', {'all': all , 'var':var2})

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})
    
def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.info(request, 'todo deleted successfully', extra_tags='success')
    return redirect('homepage')

def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'new todo successfully added', extra_tags='success')
            return redirect('homepage')
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', {'form': form})

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'your todo updated successfully', 'success')
            return redirect('details', todo_id)
    else:
        form = TodoUpdateForm(instance=todo)  # باعث میشه فرم ما با اطلاعات قبلی پر بشه
    return render(request, 'update.html', {'form':form})