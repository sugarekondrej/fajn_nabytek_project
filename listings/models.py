from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse
# Create your models here.



class Main_Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    def __str__(self):
        return self.name

def img_path_sub_category(instance, filename):
    return f"{instance.main_category}/{instance.name}/{filename}"


class Sub_Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    main_category = models.ForeignKey(Main_Category,blank = True,null =True,related_name='main_category',on_delete=models.PROTECT)
    description = models.TextField(max_length=500)
    img = models.ImageField(upload_to=img_path_sub_category, null=False, blank=False)
    img_alt = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def get_url(self):
        return reverse('products_by_category',kwargs={"main_category_slug":self.main_category.slug,"sub_category_slug":self.slug})
def img_path_sub_sub_category(instance, filename):
    return f"{instance.main_category}/{instance.sub_category}/{instance.name}/{filename}"


class Sub_sub_Category(models.Model):
    main_category = models.ForeignKey(Main_Category,blank = True,null =True,related_name='main_category_to_sub',on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    sub_category = models.ForeignKey(Sub_Category,blank=True,null=True,related_name='subcategory',on_delete=models.PROTECT)
    description = models.TextField(max_length=300)
    img = models.ImageField(upload_to=img_path_sub_sub_category, null=True, blank=True)
    img_alt = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.name
    def get_url2(self):
        return reverse('products_by_category',kwargs={"main_category_slug":self.main_category.slug,"sub_category_slug":self.sub_category.slug,"sub_sub_category_slug": self.slug})
    def get_url(self):
        return reverse('products_by_category',kwargs={"main_category_slug":self.main_category.slug,"sub_category_slug":self.sub_category.slug})
def img_path(instance, filename):
    return f"{instance.main_category}/{instance.category}/{instance.sub_category}/{filename}"


class Brand(models.Model):
    brand_id=models.IntegerField()
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

def img_path_varianta(instance, filename):
    return f"{instance.main_category}/{instance.category}/{instance.sub_category}/{instance.product_name}/{instance.varianta_img}"
def img_path_barva(instance, filename):
    return f"{instance.main_category}/{instance.category}/{instance.sub_category}/{instance.product_name}/{instance.barva_img}"

class Variants(models.Model):
    name = models.CharField(max_length=200)
    rozmery_sirka = models.IntegerField()
    rozmery_delka = models.IntegerField()
    varianta_img = models.ImageField(upload_to=img_path_varianta, null=True, blank=True)
    barva = models.CharField(max_length=200)
    barva_img = models.ImageField(upload_to=img_path_barva, null=True, blank=True)
    
    def __str__(self):
        return self.name
class Produkt(models.Model):
    ean = models.ForeignKey(Brand,blank = True,null =True,related_name='ean',on_delete=models.PROTECT)
    varianta = models.ForeignKey(Variants,blank = True,null =True,related_name='varianta',on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    main_category = models.ForeignKey(Main_Category,blank = True,null =True,related_name='mistnosti',on_delete=models.PROTECT)
    category = models.ForeignKey(Sub_Category,blank = True,null =True,related_name='category',on_delete=models.PROTECT)
    sub_category = models.ForeignKey(Sub_sub_Category,blank = True,null =True,related_name='subcategory',on_delete=models.PROTECT)
    price = models.FloatField()
    short_description= models.TextField(max_length=600)
    long_description = models.TextField(max_length=3000)
    primary_img = models.ImageField(upload_to=img_path, null=True, blank=True)
    primary_alt = models.CharField(max_length=200,null=True, blank=True)
    img1= models.ImageField(upload_to=img_path, null=True, blank=True)
    img1_alt=models.CharField(max_length=200,null=True, blank=True)
    img2= models.ImageField(upload_to=img_path, null=True, blank=True)
    img2_alt=models.CharField(max_length=200,null=True, blank=True)
    img3= models.ImageField(upload_to=img_path, null=True, blank=True)
    img3_alt=models.CharField(max_length=200,null=True, blank=True)
    img4= models.ImageField(upload_to=img_path, null=True, blank=True)
    img4_alt=models.CharField(max_length=200,null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    brand = models.ForeignKey(Brand,blank = True,null =True,related_name='brand',on_delete=models.PROTECT)
    eta = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"Kategorie: {self.category}, Produkt: {self.name}"
    def get_url(self):
        return reverse('product_detail',kwargs={"main_category_slug":self.main_category.slug,"sub_category_slug":self.category.slug,"sub_sub_category_slug": self.sub_category.slug,"product_slug":self.slug})
    def get_url_without(self):
        return reverse('product_detail',kwargs={"main_category_slug":self.main_category.slug,"sub_category_slug":self.category.slug,"product_slug":self.slug})
    # def admin_photo(self):
    #     return mark
    # def __str__(self):
    #     return mark_safe('<img src="{}" width="100" />'.format(self.primary_img.url))
    # admin_photo.short_description='Image'
    # admin_photo.allow_tags=True

