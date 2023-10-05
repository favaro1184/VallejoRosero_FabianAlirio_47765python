# VallejoRosero_FabianAlirio_47765python
Trabajo final Certificación Python CoderHouse

DESCRIPCION DEL PROYECTO:
Blog de destinos turisticos

Diseñe una pagina en la cual se pueden publicar destinos turisticos. La publicaciones solo seran realizadas por un usuario con perfil de admin, los demas usuarios solo podran visualizar las publicaciones en el blog. por defecto al cargar la pagina pide loguearse en la aplicacion. si no se cuenta con usuario se puede registrar (los usuarios creados por esta opcion no quedan con perfil de administrador). las paginas de aboutme, login, logout y registro no piden autenticacion

Acciones del usuario Admin:
tiene un menu exclusivo en el cual puede realizar:
Crear publicaciones
Consultar Sugerencias
Acceder a la consola Admin de la pagina.

tambien puede:
visualizar en la pagina del blog las publicaciones y puede ver las opciones de ver detalle, modificar o eliminar la publicacion. puede comentar las publicaciones
desde la pagina de mensajes puede enviar mensajes a cualquier usuario creado o consultar sus mensajes.
desde el dropdownlist Editar Usuario puede ver el detalle del usuario, actualizar datos, actualizar password y cargar su avatar.

En la pagina BLOG se implemento el BUSCADOR. este funciona filtrando por el campo categorias del modelo Publicacion (Por defecto hay 3, playas, hoteles, otro)

Acciones del usuario no Admin:
visualizar en la pagina del blog las publicaciones y puede ver la opcion de ver detalle. puede comentar las publicaciones
desde la pagina de mensajes puede enviar mensajes a cualquier usuario creado o consultar sus mensajes.
desde la pagina Enviar Sugerencia puede enviarle sugerencias al admin de la pagina sobre temas que desee ver en la pagina.
desde el dropdownlist Editar Usuario puede ver el detalle del usuario, actualizar datos, actualizar password y cargar su avatar.

En la pagina BLOG se implemento el BUSCADOR. este funciona filtrando por el campo categorias del modelo Publicacion (Por defecto hay 3, playas, hoteles, otro)

MODELOS CREADOS EN EL PROYECTO:
Publicacion
Comentario
Mensaje
Avatar
Sugerencia

USUARIO ADMINISTRADOR(SUPER USER): admin
PASSWORD SUPER USER: admin123*

USUARIO DE PRUEBA(no admin): andres
PASSWORD: admin123*

TECNOLOGIAS UTILIZADAS:
Front-End:
HTML 5
CSS 3
Javascript 
Bootstrap 
Back-End:
Python 
Django
Pillow

CASOS DE PRUEBA:
en el archivo excel llamado "Casos de prueba.xlsx" se encuentra el detalle de las pruebas registradas

VIDEO:
Se subio un video llamado ExplicacionProyecto.mp4 en el cual esta la explicacion del proyecto. (el viedo esta incluido en el repositorio en github)
https://drive.google.com/file/d/1HV7SDT6BY09QrrdftDoX-2_AJ_cA_m8Z/view?usp=sharing
