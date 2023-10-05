from django.shortcuts import render, redirect
from .models import Task
from .forms import add_task

# Create your views here.
def home(request):
    # Get the all objects from model
    # Here it will show the task based on the newest one to oldest one. 
    tasks = Task.objects.all().order_by('-id')
    return render(request, 'index.html',{'tasks':tasks})

def remiaining(request):
   incompleted_task = Task.objects.filter(completed = False)
   return render(request, 'remaining.html',{'tasks':incompleted_task})

def completed(request):
    completed_task = Task.objects.filter(completed = True)
    return render(request, 'completed.html',{'tasks':completed_task})

# def addTask(request):
#     if request.method == "POST":
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         due_date = request.POST.get('due_date')
#         due_time = request.POST.get('due_time')
#         completed = False
        
#         if title !="" and due_date !="" and due_time !="":
#             task = Task( 
#                         title = title,
#                         description = description,
#                         due_date = due_date,
#                         due_time = due_time,
#                         completed = completed, 
#                         )
#             task.save()
#             return redirect('home')
#         else:
#             return render(request, 'addTask.html')
#     return render(request, 'addTask.html')

def delete(request,task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'delete.html', {"task":task})

def task_detail(request, task_id):
    task = Task.objects.get(id =task_id)
    return render(request, 'task_detail.html', {"task":task})

def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.completed = not task.completed
        task.save()
        return redirect('home')


def remove_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.delete()
        return redirect('home')

def addTask(request):
    if request.method=="POST":
        task = add_task(request.POST)
        if task.is_valid():
            task.save()
            return redirect('home')
    else:
            task= add_task()
    return render(request, 'addTask.html',{'task':task})
