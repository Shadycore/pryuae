from django.shortcuts import render, HttpResponse
from django.views import generic

class Home(generic.TemplateView)
    template_name = 'baseapp/index.html'
    

def login(request):
    #return render(request,"baseapp/login.html")
   return HttpResponse("<h1> login </h1>")

def index(request):
    #return render(request,"baseapp/index.html")
    return HttpResponse("<h1> index </h1>")

def crearHaciendas(request):
    #return render(request,"baseapp/crearHaciendas.html")
    return HttpResponse("<h1> crearHaciendas </h1>")

def mantHaciendas(request):
    #return render(request,"baseapp/mantHaciendas.html")
    return HttpResponse("<h1> mantHaciendas </h1>")

def compraInsumos(request):
    #return render(request,"baseapp/compraInsumos.html")
    return HttpResponse("<h1> compraInsumos </h1>")

def repartoInsumos(request):
    #return render(request,"baseapp/repartoInsumos.html")
    return HttpResponse("<h1> repartoInsumos </h1>")

def cocechar(request):
    #return render(request,"baseapp/cocecha.html")
    return HttpResponse("<h1> cocechar </h1>")

def dashboard(request):
    #return render(request,"baseapp/dashboard.html")
    return HttpResponse("<h1> dashboard </h1>")
