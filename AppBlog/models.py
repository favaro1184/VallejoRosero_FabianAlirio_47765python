from django.db import models
from django.contrib.auth.models import User
###################################################################################################
# en el modelo Publicacion se almacena la informacion de las publicacion realizadas en el blog
# se enlaza con el modelo User por medio de un ForeingKey
class Publicacion(models.Model):
    categorias = (
    ('playas','Playas'),
    ('hoteles', 'Hoteles'),
    ('otro', 'Otro'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=15, choices=categorias, default='playas')
    cuerpo = models.TextField(null=True, blank=True)
    autor = models.CharField(max_length=40)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    imagenPublicacion = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario_id', '-fechaPublicacion']

    def __str__(self):
        return self.titulo

###################################################################################################
# en el modelo Comentario se almacena los comentarios realizados a las publicaciones. 
# se enlaza con el modelo Publicacion por medio de un ForeingKey
class Comentario(models.Model):
    comentario = models.ForeignKey(Publicacion, related_name='comentarios', on_delete=models.CASCADE, null=True)
    autor = models.CharField(max_length=70)
    mensaje = models.TextField(null=True, blank=True, max_length=300)
    comentarioFecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comentarioFecha']

    def __str__(self):
        return '%s - %s' % (self.autor, self.comentario)

###################################################################################################
# en el modelo Mensaje se almacena los mensajes que se pueden enviar entre los usuarios registrados.
# se enlaza con el modelo User por medio de 2 ForeingKey
class Mensaje(models.Model):
    emisor = models.ForeignKey(User, related_name='emisores', on_delete=models.CASCADE, null=True, blank=True)
    destinatario = models.ForeignKey(User, related_name='destinatarios', on_delete=models.CASCADE, null=True)
    mensaje = models.TextField(null=True, blank=True, max_length=300)
    fechaEnvio = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaEnvio']

    def __str__(self):
        return '%s - %s' % (self.destinatario, self.fechaEnvio)


###################################################################################################
# en el modelo Mensaje se almacena la iamgen de usuario(Avatar) de los usuarios registrados
class Avatar(models.Model):
   
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.usuario} - {self.imagen}"
    
    
###################################################################################################
# en el modelo Sugerencia se almacena las sugerencias que los diferentes usuarios registrados pueden
# hacer al admin sobre los temas que les gustarian se publicaran en la pagina
class Sugerencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    detalle = models.TextField(null=True, blank=True, max_length=300)
    fechaEnvio = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaEnvio']

    def __str__(self):
        return '%s - %s' % (self.usuario, self.fechaEnvio)
