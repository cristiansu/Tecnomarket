from django import forms
from django.forms import fields, widgets
from .models import Contacto, Producto

class ContactoForm(forms.ModelForm):

    class Meta:
        model=Contacto
        #fields=['nombre','correo','tipo_consulta','mensaje','avisos'] otro camino es con __all__
        fields='__all__'


class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'

        widgets={

            'fecha_fabricacion':forms.SelectDateWidget()
        }