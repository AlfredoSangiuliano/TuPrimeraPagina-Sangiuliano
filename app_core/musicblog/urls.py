from django.urls import path
from musicblog.views import *

app_name = "musicblog"

urlpatterns = [

    path('', inicio, name='inicio'),
    path('listar-bandas/', listar_bandas, name='listar_bandas'),
    path('crear-bandas/', crear_banda, name='crear_banda'),
    path('actualizar-bandas/<int:id>/', actualizar_banda, name='actualizar_banda'),
    path('eliminar-bandas/<int:id>/', eliminar_banda, name='eliminar_banda'),
    
    path('listar-discos/', listar_discos, name='listar_discos'),
    path('crear-discos/', crear_disco, name='crear_disco'),
    path('actualizar-discos/<int:id>/', actualizar_disco, name='actualizar_disco'),
    path('eliminar-discos/<int:id>/', eliminar_disco, name='eliminar_disco'),

    path('listar-canciones/', listar_canciones, name='listar_canciones'),
    path('crear-canciones/', crear_cancion, name='crear_cancion'),
    path('actualizar-canciones/<int:id>/', actualizar_cancion, name='actualizar_cancion'),
    path('eliminar-canciones/<int:id>/', eliminar_cancion, name='eliminar_cancion'),
]



