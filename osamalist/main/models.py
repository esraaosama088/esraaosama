from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Todo(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)  # Allow null
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name