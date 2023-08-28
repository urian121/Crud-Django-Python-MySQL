APRENDIENDO DJANDO PASO A PASO

1.  Crear entorno virtual con Python
    virtualenv env

2.  Activar ambiente virtual en Mac
    source env/bin/activate
    deactivate -->Para desactivar mi entorno virtual

3.  Instalar Djando desde Pip en el entorno virtual.
    python -m pip install Django
    pip install Django

4.  Instalar Driver para conectar Gestor de BD MySQL con Django
    pip install mysqlclient

5.  Crear el proyecto con Djando
    django-admin startproject project_core .
    El punto . es crucial porque le dice al script que instale Django en el directorio actual,
    para el cual el punto sirve de abreviatura

    - Ya en este punto se puede correr el proyecto que a creado Django,
      python manage.py runserver

6.  Crear el archivo requirements.txt para tener todos mis paquetes a la mano
    pip freeze > requirements.txt

7.  Crear mi primera aplicación en Django
    python manage.py startapp crud_libros

8.  Instalar nuestra aplicación (crud_libros) ya creada en el proyecto
    archivo settings.py
    INSTALLED_APPS = [
    ----,
    'crud_libros',
    ]

9.  Crear un Modelo en models.py de nuesta aplicacion, cada clase de nuestro modelo representa una tabla en nuestra BD (bd_crud_django) prefesiblemento los modelos
    se declaran en singular
    class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

10. Crear las migraciones que estan en mi modelo
    python manage.py makemigrations crud_libros

11. Correr migraciones
    python manage.py migrate

12. Configurar la conexión a la Base de Datos
    DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'crud_django',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '3306',
    }
    }

13. En el archivo views.py de mi apliación crear una vista (función)
    from django.http import HttpResponse

    def inicio(resquest):
    return HttpResponse("Hola Mundo", status=200)

14. Crear el archivo urls.py en la aplicación (crud_libros)
    from django.urls import path
    from . import views

    urlpatterns = [
    path('', views.home, name='home'),
    path('book-detail/<str:id>/', views.book_detail, name='book-detail'),
    path('view-book/', views.view_book, name='view-book'),
    path('add-book/', views.add_book, name='add-book'),
    path('edit-book/<str:id>/', views.edit_book, name='edit-book'),
    path('delete-book/<str:id>/', views.delete_book, name='delete-book'),

    ]

15. Ahora conectar las URLS de mi aplicación, para esto vamos al archivo uls.py del projecto
    from django.urls import path, include
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', include('crud_libros.urls')),
    ]

16. Revisar la consola y visitar la URL http://127.0.0.1:8000

17. Agregar el gitignore de Python y Djando
    https://github.com/jpadilla/django-project-template/blob/master/.gitignore

18. Crear archivo README.md para describir el proyecto etc.

19. Crear la carpeta 'templates' dentro de mi aplicacion donde estaran mis archivos .html

20. Crear la carpeta 'static' dentro de mi aplicacion, aqui estaran archivos
    estaticos (css, js, imagenes, etc..)

COMANDO ADICIONALES:

3. ver todo el historial de migraciones:
   python manage.py showmigrations

4. listar paquetes del instalador en el proyecto
   pip list
   pip freeze

5. Version de Djando en mi proyecto
   python -m django --version

6. Instalar Paquete para crear variables de entorno
   pip install django-environ

7. Correr archivo requirement.txt
   pip install -r requirements.txt

Jinja2 (una biblioteca de plantillas)
Django es un framework web gratuito y de código abierto publicado por primera vez en 2005 por
Adrian Holovaty y Simon Willison.

Django es un sofisticado framework basado en Python con configuraciones de desarrollo de pila completa,
como diseños de plantillas, solicitud y resolución de problemas, cookies, validación de formularios,
pruebas unitarias, configuración de tablas y otras funcionalidades que los desarrolladores
utilizan para crear aplicaciones web dinámicas.

Django sigue un patrón arquitectónico Modelo-Vista-Plantilla (MVT) que ayuda a los desarrolladores a
realizar tareas rutinarias o complejas de forma eficiente con poca intervención de protocolos,
administración y sistemas al crear aplicaciones de alta intensidad y sitios web basados en bases de datos.
Importante Djando genera las migraciones a partir de la informacion que existe en el modelo

---

Un proyecto en Django vs aplicacion (son como modulos de mi proyecto) en Django, en generar un
proyecto en Django esta compuesto por aplicaciones.

amazon.com -> es el proyecto
usuarios ->crear, editar, borrar, recuperar etc seria mi aplicacion o modulo
tienda ->agregar, producto, borrar, editar, enviar producto etc.

---

Los modelos Django proporciona una capa de abstracción
(los «modelos») para estructurar y manipular los datos de su aplicación web.

Crear administrador:
python manage.py createsuperuser
Luego escribir cualquier usuario y clave
Las migraciones comprenden;la autentiticafion por defecto de Django
Existen vistas de clases y vistas de funciones.
