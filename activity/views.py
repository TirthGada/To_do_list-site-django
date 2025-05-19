from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

# Create your views here.
def detail(request, item_id):
    item = get_object_or_404(Todo, id=item_id)
    return render(request, 'detail.html', {'item': item, 'title': 'Todo Details'})

def latest(request):
    latest_item = Todo.objects.order_by('-date').first()
    context = {
        'item': latest_item,
        'title': 'Latest Todo',
    }
    return render(request, 'latest.html', context)


def edit(request, item_id):
    item = get_object_or_404(Todo, id=item_id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo updated successfully!")
            return redirect('todo')
    else:
        form = TodoForm(instance=item)
    return render(request, 'edit.html', {'form': form, 'title': 'Edit Todo'})


def index(request):
    item_list = Todo.objects.order_by("date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'index.html', page)
 
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')
