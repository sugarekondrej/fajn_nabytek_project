from django.shortcuts import render
from apps import urls
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth import authenticate, logout

# Create your views here.
