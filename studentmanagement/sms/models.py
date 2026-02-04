from django.db import models
from django.contrib.auth.models import AbstractUser

#Student models
class CustomUser(AbstractUser):
    Role_Choices = [
        ('Student','Student'),
        ('Faculty','Faculty'),
        ('Admin','Admin'),
    ]
    role = models.CharField(max_length=20, choices=Role_Choices, default='Student')
    institute = models.CharField(max_length=20, default='IITRAM')
    phone_no = models.CharField(max_length = 15, blank = False, null=True)