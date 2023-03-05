from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from . import models
from listings import urls
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# listings = models.Produkt.objects.filter(typobjektu__name__startswith="Ča")
# Create your views here.

#TODO make filter to each one main category
def index(request):
    
    return render(request,'index.html')


def listings_view(request, main_category_slug=None,sub_category_slug=None,sub_sub_category_slug=None):
     categories = None
     main_categories = None
     products = None
     sub_categories = None
     sub_filter= None
     category_filter = None

     if sub_sub_category_slug!= None:
          categories = models.Sub_Category.objects.get(slug = sub_category_slug, main_category__slug=main_category_slug)
          category_filter = models.Sub_sub_Category.objects.get(slug = sub_sub_category_slug)
          main_categories = get_object_or_404(models.Main_Category, slug=main_category_slug)
          sub_categories = models.Sub_sub_Category.objects.get(slug = sub_sub_category_slug)
          products = models.Produkt.objects.filter(category=categories,main_category=main_categories,sub_category=sub_categories)
          paginator = Paginator(products, 12)
          page = request.GET.get('page')
          paged_products = paginator.get_page(page)
          product_count = products.count()
     elif sub_category_slug != None:
          categories = models.Sub_Category.objects.get(slug = sub_category_slug, main_category__slug=main_category_slug)
          main_categories = get_object_or_404(models.Main_Category, slug=main_category_slug)
          products = models.Produkt.objects.filter(category=categories,main_category=main_categories)
          sub_filter = models.Sub_sub_Category.objects.filter(sub_category__slug=sub_category_slug)
          paginator = Paginator(products, 12)
          page = request.GET.get('page')
          paged_products = paginator.get_page(page)
          product_count = products.count()
     else:
          products = models.Produkt.objects.all().order_by('id')
          paginator = Paginator(products, 13)
          page = request.GET.get('page')
          paged_products = paginator.get_page(page)
          product_count = products.count()
     context = {
        'listings': paged_products,
        'product_count': product_count,
        'category': categories,
        'category_filter':category_filter,
        'sub_categories': sub_filter,
    }
     return render(request, 'listing_view.html', context)

def product_detail(request, main_category_slug,sub_category_slug, product_slug,sub_sub_category_slug= None):
     if sub_sub_category_slug != None:

          single_product = models.Produkt.objects.get(main_category__slug=main_category_slug,category__slug=sub_category_slug,sub_category__slug=sub_sub_category_slug, slug=product_slug)
     elif sub_category_slug != None:
          single_product = models.Produkt.objects.get(main_category__slug=main_category_slug,category__slug=sub_category_slug,slug=product_slug)
     context = {
        'listing': single_product,
     }
     return render(request, 'detail_view.html', context) 
def categories(request, main_category_slug=None,sub_category_slug=None):
     categories = None
     if sub_category_slug != None:
          categories = models.Sub_Category.objects.get(main_category__slug=main_category_slug, slug=sub_category_slug)
     context = {
          "listings": categories
     }
     return render(request,"category/category_obyvaci_steny.html",context)
def cart(request):
     return render(request,'cart/cart.html')
def pokladna(request):
     return render(request,'cart/checkout.html')
def container(request):
        
        
     return render(request,'container.html')
def search(request):
     if 'keyword' in request.GET:
          keyword = request.GET["keyword"]
          if keyword:
               products = models.Produkt.objects.filter(name__icontains=keyword)
     context = {
          'listings' :products
     }
     return render(request,'listing_view.html',context)
def prodejny_vydejny(request):
     return render(request,'dev/prodejny_vydejny.html')
def zakladni_informace(request):
     return render(request,'dev/zakladni_informace.html')







#OUT OF PRODUCT VIEW, INTERNAL THINGS

def dev_kancelare(request):

     return render(request,'dev/dev-kancelare.html')

def dev_kuchyne(request):

     return render(request,'dev/dev-kuchyne.html')

def dev_nabytek(request):

     return render(request,'dev/dev-nabytek.html')

def dev_spotrebice(request):

     return render(request,'dev/dev-spotrebice.html')

def dev_spotrebice(request):

     return render(request,'dev/dev-spotrebice.html')

def developerske_projekty(request):

     return render(request,'dev/developerske-projekty.html')


