from django.db.models import fields
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "firstName", "lastName", "userName", "email", "password", "contactNo", "created_at", "updated_at")
        