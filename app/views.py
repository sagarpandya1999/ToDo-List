from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import TodoForm
from .models import Todo

# Create your views here.
def indexView(request):
    myTodo = Todo.objects.order_by('id')  # change this id to pk and chceck for that would work or not.
    form = TodoForm()

    context = {'myTodo':myTodo, 'form':form}
    return render(request, 'index.html', context)

@require_POST
def addNewTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        my_new_todo = Todo(text=request.POST['text'])
        my_new_todo.save()

    return redirect('app:apphome')

def completeTodo(request, todo_id):
    myTodo = Todo.objects.get(pk=todo_id)
    myTodo.complete = True
    myTodo.save()

    return redirect('app:apphome')

def deleteTodo(request):
    something = Todo.objects.filter(complete__exact=True)
    something.delete()

    return redirect('app:apphome')


def addBackTodo(request, todo_id):
    another = Todo.objects.get(pk=todo_id)
    another.complete = False
    another.save()

    return redirect('app:apphome')

def resetTodo(request):
    todo = Todo.objects.all()
    todo.delete()

    return redirect('app:apphome')

