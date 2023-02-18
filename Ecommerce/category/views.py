from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
# Create your views here.
"""def home(request):
    return render(request,"home.html")"""
def insertcat(request):
    if request.method =="GET":
        return render(request, "category/Insertcat.html")
    else:
        c = Category(namecat=request.POST['categoryname'])
        c.save()
        return HttpResponseRedirect("/listcat/")
def updatecat(request):
    return render(request,"category/Updatecat.html")
def deletecat(request):
    return render(request,"category/Deletecat.html")
def listcat(request):
    context = {}
    categories = Category.objects.all()
    context['categories'] = categories
    return render(request,"category/Listcat.html",context)
