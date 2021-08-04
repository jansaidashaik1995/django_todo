from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by('added_date')
    context = {
        'todos' : todos
    }
    return render(request, 'todo_app/index.html', context)

def add_todo(request):
    # print(request.POST)
    current_date = timezone.now()
    current_todo = request.POST['todo']
    print(current_date)
    print(current_todo)
    todo_object = Todo.objects.create(added_date = current_date, todo = current_todo)
    return HttpResponseRedirect('/')


def delete_todo(request, id):
    print(id)
    Todo.objects.get(id=id).delete()
    return HttpResponseRedirect('/')