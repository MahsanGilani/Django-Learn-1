from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    # path('hello/', views.say_hello),
    path('detail/<int:todo_id>/', views.detail, name='details'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('create/', views.create, name='Create')
]
