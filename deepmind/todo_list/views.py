from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_todos = List.objects.all
            messages.success(request, ('Todo item successfully added'))
            return render(request, 'home.html', {'all_todos': all_todos},)

    else:
        all_todos = List.objects.all
        return render(request, 'home.html', {'all_todos': all_todos},)

def about(request):
    return render(request, 'about.html', {})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Todo item deleted successfully'))
    return redirect('home')

def complete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    messages.success(request, ('Todo item marked as completed'))
    return redirect('home')

def uncomplete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    messages.success(request, ('Todo item marked as uncompleted'))
    return redirect('home')

