"""Nabtek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from . import views
from cart.views import cart, checkout
urlpatterns = [
    path('',views.index,name="listings"),
    path('<slug:main_category_slug>/<slug:sub_category_slug>/', views.listings_view, name='products_by_category'),
    path('<slug:main_category_slug>/<slug:sub_category_slug>/<slug:sub_sub_category_slug>', views.listings_view, name='products_by_category'),
    path('<slug:main_category_slug>/<slug:sub_category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('<slug:main_category_slug>/<slug:sub_category_slug>/<slug:sub_sub_category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('<slug:main_category_slug>/<slug:sub_category_slug>/', views.categories, name='categories'),
    # path('<slug:main_category_slug>/<slug:sub_category_slug>/', views.listings_view, name='products_by_category'),
    # path('<slug:main_category_slug>/<slug:sub_category_slug>/<slug:sub_sub_category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    # path('<slug:main_category_slug>/<slug:sub_category_slug>/<slug:product_slug>/', views.product_detail_without, name='product_detail_without'),
    path('container',views.container,name="container"),
    path("dev-kancelare",views.dev_kancelare,name="dev_kancelare"),
    path("dev-kuchyne",views.dev_kuchyne,name="dev_kuchyne"),
    path("dev-nabytek",views.dev_nabytek,name="dev_nabytek"),
    path("dev-spotrebice",views.dev_spotrebice,name="dev_spotrebice"),
    path("developerske-projekty",views.developerske_projekty,name="developerske_projekty"),
    path("kosik",cart,name="cart"),
    path("pokladna",checkout,name="pokladna"),
    path("prodejny_vydejny",views.prodejny_vydejny,name="prodejny_vydejny"),
    path("zakladni_informace",views.zakladni_informace,name="zakladni_informace"),


    
    


    # path('<int:listing_id>',views),
]
