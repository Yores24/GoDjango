from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
   
    peoples= [
      {'name':'Saurabh','age':21},
      {'name':'Saloni','age':20}
    ]
    return render(request,"index.html",context={'peoples':peoples})
 

def success_page(request):
    return HttpResponse("<h1>hey this is a success page</h1>")