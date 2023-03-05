from django.contrib import admin
from . models import Main_Category,Sub_Category,Sub_sub_Category,Produkt,Variants,Brand
# Register your models here.


class ListingProdukt(admin.ModelAdmin):
    
    list_display = ("id","ean","name","price","main_category","category","sub_category","stock","brand","eta","primary_img")
    list_display_links=("ean","name","main_category","category","sub_category","price")
 
admin.site.register(Produkt,ListingProdukt)

class Listing_main_category(admin.ModelAdmin):
    list_display=("name","description")
admin.site.register(Main_Category,Listing_main_category)

class Listing_sub_category(admin.ModelAdmin):
    list_display=("name","main_category","description")
    list_display_links=("name","main_category","description")
admin.site.register(Sub_Category,Listing_sub_category)
class Listing_brand(admin.ModelAdmin):
    list_display=("brand_id","name")
    list_display_links=("brand_id","name")
admin.site.register(Brand,Listing_brand)

class Listing_sub_sub_category(admin.ModelAdmin):
    list_display= ("id","name","main_category","description","sub_category")
    list_display_links=("main_category","name","description","sub_category")
admin.site.register(Sub_sub_Category,Listing_sub_sub_category)

class Listing_variants(admin.ModelAdmin):
    list_display=("id","rozmery_sirka","rozmery_delka","barva")
    list_display_links=("rozmery_sirka","rozmery_delka","barva")
admin.site.register(Variants,Listing_variants)