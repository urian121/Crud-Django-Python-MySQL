from django.contrib import admin

# Registrando mis Modelos
from . models import Libro

# Registrando el Modelo
admin.site.register(Libro)
