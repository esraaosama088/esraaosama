from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo, Category
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import TodoForm, CategoryForm, UserCreationForm

# Index View
def index(request):
    categories = Category.objects.all()
    todos = Todo.objects.all()
    return render(request, 'main/index.html', {'categories': categories, 'todos': todos})

# Category Views
@login_required
def category_todos(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    todos = Todo.objects.filter(category=category)
    return render(request, 'main/category_todos.html', {'category': category, 'todos': todos})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'main/category_form.html', {'form': form})

@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'main/category_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('index')
    return render(request, 'main/category_confirm_delete.html', {'category': category})

# Todo Views
@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'main/todo_form.html', {'form': form})

@login_required
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'main/todo_form.html', {'form': form})

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    return render(request, 'main/todo_confirm_delete.html', {'todo': todo})

# User Authentication Views
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'main/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})