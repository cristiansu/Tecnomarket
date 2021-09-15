from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT

# Create your models here.

class Marca(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    nuevo=models.BooleanField()
    #clave foranea con marca
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT) #on_delete podría ser cascada pero si borra un producto borraría
    #a todos los productos asociados a la misma marca, por eso se indica protect ya que así preguntará antes de eliminar.
    fecha_fabricacion=models.DateField()
    imagen=models.ImageField(upload_to='productos', null=True) #null true pq ya hay productos cargados sin fotos. la carpeta
    #productos se crea sola al interior de la carpeta media creada en la raíz

    #para que los campos se muestren en modo escritura crear función __str__ dentro de la clase Producto
    def __str__(self):
        return self.nombre

#para saber si la bd funciona okey se instala una extensión (costado izquierdo visual y se escribe sql en el buscador)
opciones_consultas=[
    [0,'consulta'],
    [1,'reclamo'],
    [2,'sugerencia'],
    [3,'felicitaciones']
]
class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    tipo_consulta=models.IntegerField(choices=opciones_consultas)
    mensaje=models.TextField()
    avisos=models.BooleanField()

    def __str__(self):
        return self.nombre