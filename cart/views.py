from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from listings.models import Produkt
from . models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist

import logging
logger = logging.getLogger(__name__)
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def cart(request,total = 0 ,quantity = 0, cart_items=None):
    # even_total = 0
    # if request.method == "POST":
    #     display_type = request.POST.get("delivery_opt", None)
    #     if display_type == "opt2":
    #         even_total = 1299
    #     elif display_type == "opt3":
    #         even_total = 1999
    delivery_price = 0
    try:
        cart = Cart.objects.get(cart_id= _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            quantity += cart_item.quantity
            total += (cart_item.product.price * cart_item.quantity)
    except ObjectDoesNotExist:
        pass # Just ignore
    context = {
        "total" : total,
        "quantity" : quantity,
        "cart_items" : cart_items,
        "delivery_price": delivery_price,
    }
    return render(request,'cart/cart.html',context)

def checkout(request,total = 0 ,quantity = 0, cart_items=None):
    # even_total = 0
    # if request.method == "POST":
    #     display_type = request.POST.get("delivery_opt", None)
    #     if display_type == "opt2":
    #         even_total = 1299
    #     elif display_type == "opt3":
    #         even_total = 1999
    delivery_price = 0
    try:
        cart = Cart.objects.get(cart_id= _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            quantity += cart_item.quantity
            total += (cart_item.product.price * cart_item.quantity)
    except ObjectDoesNotExist:
        pass # Just ignore
    context = {
        "total" : total,
        "quantity" : quantity,
        "cart_items" : cart_items,
        "delivery_price": delivery_price,
    }
    return render(request,'cart/checkout.html',context)

def add_cart(request,product_id):
    product = Produkt.objects.get(id=product_id)
    try:
        cart= Cart.objects.get(cart_id=_cart_id(request)) #get cart using session id
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity += 1
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product,quantity=1,cart=cart)
    cart_item.save()
    return redirect('cart')
    # exit()
    # return redirect('cart')

def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Produkt,id=product_id)
    cart_item = CartItem.objects.get(cart=cart,product=product)
    
    if cart_item.quantity >1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect("cart")

def remove_product(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Produkt,id=product_id)
    cart_item = CartItem.objects.get(cart=cart,product=product)
    
    cart_item.delete()
    
    return redirect("cart")