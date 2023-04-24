from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect
from datetime import datetime
# Create your views here.

def gettime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")
def homePage(request):
    allToDoItems = TodoListItem.objects.all()
    return render(request, 'index.html', {'all_items': allToDoItems})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = f"{x}")
    new_item.save()
    return HttpResponseRedirect('/')

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/')