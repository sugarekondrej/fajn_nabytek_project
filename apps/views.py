from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth import authenticate, logout


def new_order(request):

     return render(request,'admin/apps/new-order.html')