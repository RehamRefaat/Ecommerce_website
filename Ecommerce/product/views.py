from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from category.models import *

# Create your views here.
def home(request):
    return render(request,"home.html")


def insert(request):
    if request.method=='GET':
        context = {}
        categories = Category.objects.all()
        context['categories'] = categories
        return render(request, "product/Insert.html",context)
    else:
        Product.objects.create(namepro=request.POST['productname'],catid=Category.objects.get(Idcat=request.POST['category']))
        return HttpResponseRedirect("/list/")
def update(request):
    if request.method=='GET':
        context = {}
        productes = Product.objects.all()
        context['productes'] = productes
        return render(request, "product/Update.html",context)
    else:
        Product.objects.filter(Idpro=request.POST['product']).update(namepro=request.POST['proname'])
        return HttpResponseRedirect("/update/")


def delete(request):
    if request.method =="GET":
        context = {}
        products = Product.objects.all()
        context['products'] = products
        return render(request, "product/Delete.html",context)
    else:
        Product.objects.filter(Idpro=request.POST['deletepro'])[0].delete()
        return HttpResponseRedirect("/list/")

def listp(request):
    context={}
    products=Product.objects.all()
    context['products']=products
    return render(request, "product/List.html",context)
