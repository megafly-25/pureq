from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from agencia_turismo.models import Galeria_agencia, Paquete_turistico_agencia,Servicios_agencia
from django.contrib import messages

# Create your views here.
def Principal(request):
    paquete=Paquete_turistico_agencia.objects.order_by('nombre')
    lista_paquetes=Paquete_turistico_agencia.objects.order_by('nombre')[:4]
    servicios=Servicios_agencia.objects.get_queryset().order_by('nombre')
    return render(request,"principal.html",{'paquetes':paquete,'lista_paquetes':lista_paquetes,'servicios':servicios})
def Nosotros(request):
    return render(request,"nosotros.html")
def Paquetes_Turisticos(request):
    paquetes=Paquete_turistico_agencia.objects.order_by('nombre')
    return render(request,"paquetes_turisticos.html",{'paquetes':paquetes})

def Paquete(request,slug):
    paquetes=Paquete_turistico_agencia.objects.filter(slug_paquete=slug)
    lista_paquetes=Paquete_turistico_agencia.objects.order_by('nombre')[:4]
    servicios=Servicios_agencia.objects.get_queryset().order_by('nombre')
    return render(request,"paquete.html",{'paquetes':paquetes,'lista_paquetes':lista_paquetes,'servicios':servicios})
def Tips_viaje(request):

    return render(request,"tips_viaje.html")
def Galeria_Imagenes(request):

    return render(request,"galeria_imagenes.html")

def Eventos_Turisticos(request):

    return render(request,"eventos_turisticos.html")

def Contacto(request):
    
    return render(request,"contacto.html")




