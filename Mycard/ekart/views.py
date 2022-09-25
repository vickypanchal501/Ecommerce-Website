from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.


def index(request):
    allprods = []
    catprods = Product.objects.values("category", "id")
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslide = (n//4 + ceil((n/4)-(n//4)))
        allprods.append([prod,range(1,nslide),nslide])

    # allprods = [[product , range(1,nslide), nslide],
    #             [product , range(1,nslide), nslide]]
    params = {"allprods": allprods}

    # params  ={"no_of_slide":nslide,"product" : product, "range": range(1,nslide)}

    return render(request, "ekarts\index.html", params)


def contect(request):
    return HttpResponse("this is a contect")


def about(request):
    return render(request, "ekarts\About.html")


def tracker(request):
    return HttpResponse("this is a tracker")


def search(request):
    return HttpResponse("this is a search")


def productview(request):
    return HttpResponse("this is a productview")


def checkout(request):
    return HttpResponse("this is a checkout")
