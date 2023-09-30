from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup_page"),
    path('', views.home, name='home_page'),
    path('tasks/', views.tasks, name="task_page"),
    path('tasks_completed/', views.task_completed, name="task_completed"),
    path('logout/', views.cerrar_sesion, name="logout_page"),
    path('signin/', views.signin, name="signin_page"),
    path('tasks/create', views.create_task, name='create_tasks'),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete',
         views.complete_task, name='task_complete'),
    path('tasks/<int:task_id>/delete',
         views.delete_task, name='task_delete'),
]
