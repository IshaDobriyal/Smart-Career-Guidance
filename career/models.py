from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):

    full_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=128)

    education = models.CharField(max_length=100)

    skills = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
