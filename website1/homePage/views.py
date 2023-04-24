from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect
from datetime import datetime
from django.core.mail import send_mail
from datetime import date
# Create your views here.

def emailList(request):
    email = request.POST.get("email")

    allLogs = TodoListItem.objects.all()
    itemList = '\n'.join([i.content for i in allLogs])
    send_mail(f'Logs for: {date.today()}',itemList, 'bigbelta1234@gmail.com', [email], fail_silently=False )
    return HttpResponseRedirect('/')

def gettime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")
def homePage(request):
    allToDoItems = TodoListItem.objects.all()
    return render(request, 'index.html', {'all_items': allToDoItems})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = f"{x} at: {gettime()}")
    new_item.save()
    return HttpResponseRedirect('/')

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/')