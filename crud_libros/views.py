from django.shortcuts import render
from django.http import HttpResponse


# Mis Vistas (Funciones)


def inicio(resquest):
    return render(resquest, "bases.html")
    # return HttpResponse("Hola Mundo", status=200)
