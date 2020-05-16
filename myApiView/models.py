from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone

from .managers import *
# Create your models here.


class CustomerModel(AbstractBaseUser,PermissionsMixin):
    '''Model for creating customer'''
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    customer_address = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

