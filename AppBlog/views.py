from django.shortcuts import render
from .forms import CambiarPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import UserRegisterForm, AvatarFormulario
from .models import Publicacion, Comentario, Mensaje, Avatar, Sugerencia
from django.http import HttpResponse


############################################################################################################################################
# PAGINA DE INICIO
@login_required
def inicio(request):
    return render(request, "AppBlog/inicio.html")

############################################################################################################################################
# MANEJO DE LOS USUARIOS
#lOGIN
class LoginPagina(LoginView):
    template_name = 'AppBlog/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('Inicio')
    
    def get_success_url(self):
        return reverse_lazy('Inicio')
    
#REGISTER
def registro(request):
      if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppBlog/registro_exitoso.html" ,  {"mensaje":"Usuario Creado"})
      else:     
            form = UserRegisterForm()    
      return render(request,"AppBlog/registro.html" , {"res":form})
  
#UPDATE DATOS PERSONALES
class ActualizarDataUser(LoginRequiredMixin, UpdateView):
    template_name = "AppBlog/actualizar_data_user.html"
    model = User
    fields = ["email", 'last_name', 'first_name']
    success_url = "/AppBlog/inicio/"

#UPDATE DATOS PASSWORD
class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    form_class = CambiarPasswordForm
    template_name = "AppBlog/actualizar_pass_user.html"
    success_url = "/AppBlog/inicio/"
    
#DETALLE DEL USUARIO
class UsuarioDetalle(LoginRequiredMixin, DetailView): 
    model = User
    fields = ["id", "username", "email", "first_name", "last_name"]
    template_name = "AppBlog/detalle_user.html"
    success_url = "/AppBlog/usuario/detalle/"
    
    
############################################################################################################################################
# MANEJO DEL BLOG
class ListaBlog(LoginRequiredMixin, ListView):
    context_object_name = 'blog_page'
    queryset = Publicacion.objects.all()
    template_name = "AppBlog/blog_page.html"
    login_url = '/AppBlog/blog_page/'

class DetalleBlog(LoginRequiredMixin, DetailView):
    model = Publicacion
    context_object_name = 'blog'
    template_name = 'AppBlog/blog_detalle.html'

class PublicarBlog(LoginRequiredMixin, CreateView): 
    model = Publicacion
    fields = ['titulo', 'subtitulo', 'categoria', 'cuerpo', 'autor','imagenPublicacion'] 
    success_url = '/AppBlog/blog_page/'
    template_name = 'AppBlog/blog_creacion.html'
    
    def form_valid(self, form):
        form.instance.usuario_id = self.request.user.id
        return super(PublicarBlog, self).form_valid(form)
    
class ActualizarBlog(LoginRequiredMixin, UpdateView):
    model = Publicacion
    fields = ['titulo', 'subtitulo', 'categoria', 'cuerpo', 'autor','imagenPublicacion'] 
    success_url = "/AppBlog/blog_page/"
    template_name = 'AppBlog/blog_modificacion.html'
    
class BorrarBlog(LoginRequiredMixin, DeleteView):
    model = Publicacion
    fields = ['titulo', 'subtitulo', 'categoria', 'cuerpo', 'autor','imagenPublicacion'] 
    success_url = "/AppBlog/blog_page/"
    template_name = 'AppBlog/blog_eliminacion.html'
    

def busqueda_categoria(request):
    if request.GET["categoria"]:
        categoria = request.GET["categoria"]
        categoria_resultado = Publicacion.objects.filter(categoria__iexact=categoria)
        
        return render(request, "AppBlog/blog_categoria.html", {"categoria": categoria, "res":categoria_resultado})
    
    else: 
        return HttpResponse("Diligencia el campo de categoria")
 
    return render(request, "AppBlog/blog_categoria.html")


############################################################################################################################################
# COMENTARIOS DE PUBLICACIONES  
class ComentarPublicacion(LoginRequiredMixin, CreateView):
    model = Comentario
    fields = ['autor', 'mensaje'] 
    success_url = "/AppBlog/blog_page/"
    template_name = 'AppBlog/blog_comentario.html'

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarPublicacion, self).form_valid(form)


############################################################################################################################################
# ENVIO DE MENSAJES ENTRE USUARIOS
class EnviarMensaje(LoginRequiredMixin, CreateView): 
    model = Mensaje
    fields = ['destinatario', 'mensaje'] 
    success_url = '/AppBlog/blog_page/'
    template_name = 'AppBlog/enviar_mensaje.html'
    
    def form_valid(self, form):
        form.instance.emisor_id = self.request.user.id
        return super(EnviarMensaje, self).form_valid(form)

class ConsultarMensajes(LoginRequiredMixin, ListView):
    context_object_name = 'mensajes'
    template_name = "AppBlog/consultar_mensajes.html"
    login_url = '/AppBlog/blog_page/'
    
    def get_queryset(self):
        user_id = self.request.user.id
        if user_id:
            return Mensaje.objects.filter(destinatario=user_id)
        return super().get_queryset()

class EliminarMensaje(LoginRequiredMixin, DeleteView):
    model = Mensaje
    fields = ['destinatario', 'mensaje', 'emisor'] 
    success_url = "/AppBlog/consultar_mensajes/"
    template_name = 'AppBlog/eliminar_mensaje.html'

############################################################################################################################################
# AVATAR DE LOS USUARIOS
@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        
        if form.is_valid():
            usuarioActual = User.objects.get(username = request.user)
            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])
            avatar.save()
            return render(request, "AppBlog/inicio.html")
        else:
            form = AvatarFormulario()
    form = AvatarFormulario()    
    return render(request, "AppBlog/cargar_avatar.html", {"res":form})


############################################################################################################################################
# ENVIO DE MENSAJES ENTRE USUARIOS
class EnviarSugerencia(LoginRequiredMixin, CreateView): 
    model = Sugerencia
    fields = ['detalle'] 
    success_url = '/AppBlog/inicio/'
    template_name = 'AppBlog/enviar_mensaje.html'
    
    def form_valid(self, form):
        form.instance.usuario_id = self.request.user.id
        return super(EnviarSugerencia, self).form_valid(form)

class ConsultarSugerencias(LoginRequiredMixin, ListView):
    context_object_name = 'sugerencias'
    template_name = "AppBlog/consultar_sugerencias.html"
    login_url = '/AppBlog/inicio/'
    
    def get_queryset(self):
        user_id = self.request.user.id
        if user_id:
            return Sugerencia.objects.all()
        return super().get_queryset()

class EliminarSugerencia(LoginRequiredMixin, DeleteView):
    model = Sugerencia
    fields = ['detalle', 'usuario'] 
    success_url = "/AppBlog/consultar_sugerencias/"
    template_name = 'AppBlog/eliminar_sugerencia.html'

#<a href="{% url 'EliminarMensaje' mensaje.id %}">Eliminar</a>

############################################################################################################################################
# ABOUT ME

def about_me(request):
    return render(request, 'AppBlog/acerca_de_mi.html')


        
