from django.contrib import admin
from . models import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.urls import path

admin.site.register(NewOrder)