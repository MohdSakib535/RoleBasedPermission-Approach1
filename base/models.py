# myapp/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Principal', 'Principal'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Custom related_name to avoid conflicts
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Custom related_name to avoid conflicts
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')

    def __str__(self):
        return self.username
    

class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    principal = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'Principal'})

    def __str__(self):
        return self.name
    

    
class Attendance(models.Model):
    user_Data=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='user_data')
    date=models.DateField()
    present=models.BooleanField(default=False)
    absent=models.BooleanField(default=False)





