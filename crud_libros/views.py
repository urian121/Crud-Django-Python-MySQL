from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from . models import Libro


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
    libro = Libro.objects.get(id=id)
    # libro = Libro.objects.filter(id=request.id)
    data = {"libro": libro}
    return render(request, "libros/detail.html", data)


def view_form_update(request, id):
    libro = Libro.objects.get(id=id)
    data = {"libro": libro}
    return render(request, "libros/form_update.html", data)


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
