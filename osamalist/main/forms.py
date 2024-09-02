from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Todo, Category

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'description', 'deadline', 'category', 'status']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']