# MusicBlog

MusicBlog es una aplicación web desarrollada con Python y Django. 
Su propósito es ofrecer un sistema de gestión de canciones, discos y bandas, permitiendo realizar operaciones básicas de ABML (Alta, Baja, Modificación y Lectura) para cada uno de estos elementos.

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instalado lo siguiente:

- Python 3.11 o superior
- Django 3.x o superior
- asgiref==3.8.1
- Django==5.1.4
- sqlparse==0.5.2
- tzdata==2024.2

## Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

1. Clona este repositorio:

   git clone https://github.com/AlfredoSangiuliano/TuPrimeraPagina-Sangiuliano.git

2. Crea un Virtual envoronment de python (opcional recomendable)

   python -m venv .venv

3. Instala los paquetes de requirements.py

   pip install -r requirements.txt

3. Ejecuta el comando runserver dentro de la carpeta app_core de la siguiente manera: 

   python .\manage.py runserver

4. En una ventana de Chrome abre el servicio de manera local en localhost: 

   http://127.0.0.1:8000/