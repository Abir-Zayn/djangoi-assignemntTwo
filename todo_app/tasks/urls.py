from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home, name='home'),
     path('remaining',views.remiaining, name='remaining'),
    path('completed',views.completed, name='completed'),
    path('addTask',views.addTask, name='addTask'),
    path('delete_task/<str:task_id>',views.delete, name='delete'),
    path('detail/<str:task_id>',views.task_detail, name='task_detail'),
    path('toggle_complete/<str:task_id>',views.toggle_complete, name='toggle_complete'),
    path('remove_task/<str:task_id>',views.remove_task, name="remove_task"),
]
