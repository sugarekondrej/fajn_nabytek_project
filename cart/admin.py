from django.contrib import admin
from . models import Cart,CartItem
# Register your models here.
class ListingCart(admin.ModelAdmin):
    list_display=("cart_id","date_added")
    list_display_links = ("cart_id","date_added")


admin.site.register(Cart,ListingCart)

class ListingCartItem(admin.ModelAdmin):
    list_display=("product","quantity","cart")
    list_display_links = ("product","quantity","cart")
admin.site.register(CartItem,ListingCartItem)
