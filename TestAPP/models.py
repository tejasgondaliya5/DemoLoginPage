import email
from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=100, blank=True)
    lastName = models.CharField(max_length=100, blank=True)
    userName = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    contactNo = models.CharField(max_length=100, blank=True)
    isDeleted = models.CharField(default="0", max_length=1)  # It is Bydefualt 0 and data is Deleted then value is 1
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.email