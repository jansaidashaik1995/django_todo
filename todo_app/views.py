from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Todo
from todo_app.forms import UserForm, UserProfileInfoForm
# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by('added_date')
    context = {
        'todos' : todos
    }
    return render(request, 'todo_app/index.html', context)


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }

    return render(request, 'todo_app/register.html', context)



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