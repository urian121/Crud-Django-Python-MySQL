from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from . models import Libro


import requests


# Mis Vistas (Funciones)


def inicio(request):
    return render(request, "bases.html")
    # return HttpResponse("Hola Mundo", status=200)


def view_form_add_libro(request):
    return render(request, "libros/form_add.html")


def add_saved_libro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        precio = request.POST.get('precio')

        nuevo_libro = Libro(titulo=titulo, autor=autor, precio=precio)
        nuevo_libro.save()

        return redirect('list_libros')

    # Renderiza el formulario en caso de método GET
    return render(request, 'formulario_libro.html')


def list_libros(request):
    libros = Libro.objects.all()
    print(libros)
    books = Libro.objects.all().values()
    print(books)

    books_2 = list(Libro.objects.all().values())
    print(books_2)
    libros_3 = list(Libro.objects.values())
    print(libros_3)
    """
    for libro in libros:
        print(libro)
    """
    data = {"libros": libros}
    # libros = list(Libro.objects.values())
    return render(request, "libros/list.html", data)


def view_detail_libro(request, id):
    try:
        libro = Libro.objects.get(id=id)
        # libro = Libro.objects.filter(id=request.id)
        data = {"libro": libro}
        return render(request, "libros/detail.html", data)
    except Libro.DoesNotExist:
        # Manejar el caso en el que no existe el registro
        error_message = f"no existe ningún registro para la busqueda id: {id}"
        return render(request, "libros/error.html", {"error_message": error_message})


def view_form_update(request, id):
    try:
        libro = Libro.objects.get(id=id)
        data = {"libro": libro}
        return render(request, "libros/form_update.html", data)
    except ObjectDoesNotExist:
        error_message = f"El libro con id: {id} no existe."
        return render(request, "libros/error.html", {"error_message": error_message})


def update_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == "POST":
        libro.titulo = request.POST["titulo"]
        libro.autor = request.POST["autor"]
        libro.save()
    return redirect('list_libros')


def delete_libro(request, id):
    # Estoy borran por el metodo GET, la informacion viaja en la URL
    libro = Libro.objects.get(id=id)
    libro.delete()

    return redirect('list_libros')


def form_api(request):
    return render(request, "libros/api/form_login.html")


def login_api(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        api_url = "http://192.168.10.20/api-token-auth/"
        data = {
            "username": username,
            "password": password
        }

        try:
            response = requests.post(api_url, data=data)
            response.raise_for_status()  # Raises an exception for non-2xx status codes

            # Assuming a successful response has status code 200
            return HttpResponse("Login successful")

        except requests.exceptions.RequestException as e:
            # Handle request-related exceptions here
            return HttpResponse("Login failed: {}".format(e))

    # Render the form in case of a GET request
    return HttpResponse('Render the login form here')


def saludar(request):
    # pass
    return HttpResponse("Hola Mundo", status=200)


""" 
def emp(request):
	if request.method == "POST":
		form = EmployeeForm (request.POST) # here "form" is one varible
		if form.is_valid():
			try:
				form.save()
				return redirect("/show")
			except:
				pass
	else:
		form = EmployeeForm()
	return render(request,"index.html",{'form':form})
 
 
def update(request,id):
	employee = Employee.objects.get(id=id)
	form = EmployeeForm(request.POST, instance=employee)
	if form.is_valid():
		form.save()
		return redirect('/show')
	return render(request,"edit.html",{'employee':employee})
 
def tutorial_detail(request, pk):
    try: 
        tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
"""
