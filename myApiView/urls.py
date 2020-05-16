from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path('customers',CustomerView.as_view()),
    path('customers/<int:pk>',CustomerView.as_view())
]
