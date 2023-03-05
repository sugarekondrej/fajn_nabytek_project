from .models import *
def obyvaci_pokoj(request):
    mistnost = Sub_Category.objects.filter(main_category__name__icontains="Obývací")
    return dict(obyvaci_pokoj=mistnost)

def loznice(request):
    mistnost = Sub_Category.objects.filter(main_category__name__icontains="Ložnice")
    return dict(loznice=mistnost)

def kuchyne(request):
    mistnost = Sub_Category.objects.filter(main_category__name__icontains="Kuchyně")
    return dict(kuchyne=mistnost)

def detsky_pokoj(request):
    mistnost = Sub_Category.objects.filter(main_category__name__icontains="Dětský pokoj")
    return dict(detsky_pokoj=mistnost)

def ostatni(request):
    mistnost = Sub_Category.objects.filter(main_category__name__icontains="Ostatní")
    return dict(ostatni=mistnost)

def ob_links(request):
    links = Sub_sub_Category.objects.filter(main_category__name__icontains="Obývací")
    return dict(ob_links=links)

def sedaci_soupravy_links(request):
    links = Sub_sub_Category.objects.filter(sub_category__name__icontains="Sedací")
    return dict(sedaci_soupravy_links=links)

def obyvaci_steny_links(request):
    links = Sub_sub_Category.objects.filter(sub_category__name__icontains="Obývací")
    return dict(obyvaci_steny_links=links)

def postele_links(request):
    links = Sub_sub_Category.objects.filter(sub_category__name__icontains="Postele")
    return dict(postele_links=links)

def kuchynske_linky_links(request):
    links = Sub_sub_Category.objects.filter(sub_category__name__icontains="Kuchyňské linky")
    return dict(kuchynske_linky_links=links)

def jidelni_stolky_links(request):
    links = Sub_sub_Category.objects.filter(sub_category__name__icontains="Jidelní stolky")
    return dict(jidelni_stolky_links=links)

def spotrebice_links(request):
    links = Sub_sub_Category.objects.filter(sub_category__name__icontains="Spotřebiče")
    return dict(spotrebice_links=links)
def postele(request):
    links = Sub_sub_Category.objects.filter(sub_category__name__icontains="Postele",main_category__name__icontains="Dětský pokoj")
    return dict(postele=links)
