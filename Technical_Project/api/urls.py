from django.urls import path
from . import views


urlpatterns = [
    path('', views.tasklist, name='task-list'),
    path('<int:id>', views.taskdetail, name='task_detail'),
    path('create', views.taskcreate, name='task_create'),
    path('update/<int:id>', views.taskupdate, name='task_update'),
    path('delete/<int:id>', views.taskdelete, name="task_delete")
]