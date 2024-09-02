from django.urls import path
from .views import (
    index,
    category_todos,
    todo_create,
    todo_update,
    todo_delete,
    category_create,
    category_update,
    category_delete,
    user_login,
    user_logout,
    register
)

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', category_todos, name='category_todos'),
    path('todo/new/', todo_create, name='todo_create'),
    path('todo/<int:pk>/edit/', todo_update, name='todo_update'),
    path('todo/<int:pk>/delete/', todo_delete, name='todo_delete'),
    path('category/new/', category_create, name='category_create'),
    path('category/<int:pk>/edit/', category_update, name='category_update'),
    path('category/<int:pk>/delete/', category_delete, name='category_delete'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]