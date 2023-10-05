from django.contrib import admin
from .models import Publicacion, Comentario, Mensaje, Avatar, Sugerencia

###################################################################
#Registramos los modelos creados para poder visualizarlos desde
#el panel de Admin

admin.site.register(Publicacion)

admin.site.register(Comentario)

admin.site.register(Mensaje)

admin.site.register(Avatar)

admin.site.register(Sugerencia)
