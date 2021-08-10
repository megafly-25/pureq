from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Usuario_agencia(models.Model):
    nombre=models.CharField(max_length=100,help_text="Ingrese su Nombre:")
    apellido=models.CharField(max_length=100,help_text="Ingrese su Apellido:")
    celular=models.IntegerField(max_length=9,help_text="Ingrese su Numero de Celular")
    correo=models.EmailField(max_length=100,help_text="Ingrese su Correo Electronico")
    ciudad=models.CharField(max_length=100,help_text="Ingrese su ciudad")
    mensaje=models.CharField(max_length=300,help_text="Ingrese Un texto")
    def __str__(self):
        return self.nombre
class Departamento_agencia(models.Model):
    nombre = models.CharField(max_length=100,help_text="Ingrese el Departamento")

    def __str__(self):
        return self.nombre

class Provincia_agencia(models.Model):
    nombre=models.CharField(max_length=100,help_text="Ingrese la Provincia")
    departamento=models.ForeignKey(Departamento_agencia, on_delete=models.CASCADE)    

    def __str__(self):
        return self.nombre
class Distrito_agencia(models.Model):
    nombre=models.CharField(max_length=100,help_text="Ingrese el Distrito")
    provincia=models.ForeignKey(Provincia_agencia(), on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
class Galeria_agencia(models.Model):
    nombre=models.CharField(max_length=100,help_text="Ingrese el Distrito")
    img1=models.ImageField(verbose_name="Subir Imagen 1",blank=True,null=True)
    img2=models.ImageField(verbose_name="Subir Imagen 2",blank=True,null=True)
    img3=models.ImageField(verbose_name="Subir Imagen 3",blank=True,null=True)
    img4=models.ImageField(verbose_name="Subir Imagen 4",blank=True,null=True)
    img5=models.ImageField(verbose_name="Subir Imagen 5",blank=True,null=True)
    distrito=models.ForeignKey(Distrito_agencia(), on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
class Evento_agencia(models.Model):
    nombre=models.CharField(max_length=250,help_text="Nombre del Evento Turistico")
    fecha=models.DateField(auto_now=False, auto_now_add=False)
    distrito=models.ForeignKey(Distrito_agencia(), on_delete=models.CASCADE)
    galeria=models.ForeignKey(Galeria_agencia(), on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
class Recorrido_agencia(models.Model):
    nombre=models.CharField(max_length=150,help_text="Nombre del Recorrido")
    Recorrido1=models.CharField(max_length=150,help_text="Primera Parada",blank=True,null=True )
    Recorrido2=models.CharField(max_length=150,help_text="Primera Parada",blank=True,null=True)
    Recorrido3=models.CharField(max_length=150,help_text="Primera Parada",blank=True,null=True)
    Recorrido4=models.CharField(max_length=150,help_text="Primera Parada",blank=True,null=True)
    Recorrido5=models.CharField(max_length=150,help_text="Primera Parada",blank=True,null=True)
    Recorrido6=models.CharField(max_length=150,help_text="Primera Parada",blank=True,null=True)
    Recorrido7=models.CharField(max_length=150,help_text="Primera Parada",blank=True,null=True)
    Recorrido8=models.CharField(max_length=150,help_text="Primera Parada",blank=True,null=True)
    Recorrido9=models.CharField(max_length=150,help_text="Primera Parada",blank=True,null=True)
    Recorrido10=models.CharField(max_length=150,help_text="Primera Parada",blank=True,null=True)
    def __str__(self):
        return self.nombre
class Servicios_agencia(models.Model):
    nombre=models.CharField(max_length=100,help_text="Ingrese el Distrito")
    def __str__(self):
        return self.nombre
class Paquete_turistico_agencia(models.Model):
    nombre=models.CharField(max_length=100,help_text="Ingrese el Distrito")
    slug_paquete=models.SlugField(null=True,blank=True)
    hora_salida=models.TimeField()
    hora_entrada=models.TimeField()
    precio=models.FloatField(max_length=100,help_text="Ingrese el precio en Soles")
    distrito=models.ForeignKey(Distrito_agencia(), on_delete=models.CASCADE)
    servicio=models.ManyToManyField(Servicios_agencia())
    recorrido=models.ForeignKey(Recorrido_agencia(), on_delete=models.CASCADE)
    galeria=models.ForeignKey(Galeria_agencia(), on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

def slug_generator_paquete(sender,instance,*args,**kwargs):
    if instance.slug_paquete:
        return
    instance.slug_paquete=slugify(instance.nombre)
pre_save.connect(slug_generator_paquete,sender=Paquete_turistico_agencia)