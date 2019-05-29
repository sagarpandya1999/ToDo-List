from django.urls import path
from . import views
app_name = 'app'

urlpatterns = [

    path('', views.indexView, name='apphome'),
    path('add', views.addNewTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='comp'),
    path('delete', views.deleteTodo, name='delete'),
    path('adddback/<todo_id>', views.addBackTodo, name='addBack'),
    path('resetTodo', views.resetTodo, name='resetTodo'),

]