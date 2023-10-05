from django.urls import path
from AppBlog.views import *
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    
    ###############################################################################################
    #manejo usuarios
    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='AppBlog/logout.html'), name='logout'),
    path('registro/', views.registro, name="Registro"),
    path('usuario/actualizarData/<int:pk>', ActualizarDataUser.as_view(), name="ActualizarDataUser"),
    path('usuario/actualizarPass/<int:pk>', CambiarPassword.as_view(), name="ActualizarPasswordUser"),
    path('usuario/detalle/<int:pk>', UsuarioDetalle.as_view(), name="DetalleUsuario"),
    
    ###############################################################################################
    #manejo Blog
    path('blog_page/', ListaBlog.as_view(), name='BlogPage'),
    path('blog_detalle/<int:pk>/', DetalleBlog.as_view(), name='BlogDetalle'),
    path('blog_creacion/', PublicarBlog.as_view(), name="BlogCreacion"),
    path('blog_modificacion/<int:pk>', ActualizarBlog.as_view(), name="BlogActualizacion"),
    path('blog_eliminacion/<int:pk>', BorrarBlog.as_view(), name="BlogEliminacion"),
    
    #buscador
    path('blog_categoria/', views.busqueda_categoria, name="BlogCategoria"),
    
    ###############################################################################################
    #manejo Comentarios
    path('blog_detalle/<int:pk>/comentario/', ComentarPublicacion.as_view(), name='BlogComentario'),
    
    ###############################################################################################
    #manejo Mensajes
    path('enviar_mensaje/', EnviarMensaje.as_view(), name="EnviarMensaje"),
    path('consultar_mensajes/', ConsultarMensajes.as_view(), name="ConsultarMensaje"),
    path('eliminar_mensaje/<int:pk>', EliminarMensaje.as_view(), name="EliminarMensaje"),
    
    ###############################################################################################
    #manejo avatar
    path('cargar_avatar/', views.agregar_avatar, name="CargarAvatar"),
    
    ###############################################################################################
    #manejo Sugerencias
    path('enviar_sugerencia/', EnviarSugerencia.as_view(), name="EnviarSugerencia"),
    path('consultar_sugerencias/', ConsultarSugerencias.as_view(), name="ConsultarSugerencia"),
    path('eliminar_sugerencia/<int:pk>', EliminarSugerencia.as_view(), name="EliminarSugerencia"),
    
    
    ###############################################################################################
    #about me
    path('about_me/', views.about_me, name="AboutMe"),
]