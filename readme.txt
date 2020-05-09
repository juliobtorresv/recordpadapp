Bitacora RecordPadApp

Fecha: 3/05/2020        User: JT

Clonación del repositorio:

git clone https://github.com/juliobtorresv/recordpadapp.git recordpadapp

Fecha: 5/5/2020     User:PT

1. Creación de la app registroPersonas.
2. DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'recoad',
        'USER': 'admin',
        'PASSWORD': 'r3co4d',
        'HOST': 'localhost',
        'PORT': '3306',
    }
3. creacion del index.html
4. creacion directorios templates, css,img, js dentro de la app registroPersonas

----------------------------------------------

06/05/2020
Pantalla de bienvenida
Validación de usuario y clave importando las clases de django
from django.contrib.auth import authenticate
PTO

----------------------------------------------
06/05/2020          JT
Modificación a la conexión de base de datos mysql
para que me funcione en mi equipo. Dejo el archivo configurado
debería fucionar sin cambios en tu equipo. Dejo comentado la 
configuracion original 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'recoad',
        'USER': 'admin',
        'PASSWORD': 'r3co4d',
        'HOST': '127.0.0.1', # Cambio el localhost por IP (JT)
        'PORT': '3306',
    }
}    

---------------------------------------------