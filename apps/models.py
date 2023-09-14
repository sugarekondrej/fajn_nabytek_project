from django.db import models
from django.utils.safestring import mark_safe
from django.urls import path,reverse,include
from django.template.response import TemplateResponse
from django.contrib import admin
# Create your models here.

class NewOrder(models.Model):
    def new_order(request):

        return render(request,'admin/apps/new-order.html')