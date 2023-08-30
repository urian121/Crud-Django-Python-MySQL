from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('formulario-agregar-nuevo-libro/', views.view_form_add_libro,
         name='form_agregar_libro'),

    path('guardar-nuevo-libro/', views.add_saved_libro, name='agregar_libro'),

    path('lista-libros/', views.list_libros, name='list_libros'),
    path('detalle-libro/<str:id>/',
         views.view_detail_libro, name='view_detail_libro'),


    path('form-actualizar-libro/<str:id>/',
         views.view_form_update, name='view_form_update'),

    path('actualizar-libro/<str:id>/', views.update_libro, name='update_libro'),
    path('borrar-libro/<int:id>', views.delete_libro, name="borrar_libro"),



    # Api don Edi
    path('api/form/', views.form_api, name='form_api'),
    path('api/form-login/', views.login_api, name='login_api'),

]
