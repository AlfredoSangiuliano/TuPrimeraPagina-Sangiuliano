from django.shortcuts import render,redirect, get_object_or_404
from musicblog.models import Banda,Cancion,Disco
from .forms import BandaForm,DiscoForm,CancionForm

 ### INICIO Vistas de bandas ###

def inicio(request):
    return render(request, 'musicblog/inicio.html')

def listar_bandas(request):
    bandas = Banda.objects.all()
    return render(request, 'musicblog/banda_listar.html', {'bandas':bandas})

def crear_banda(request):
    if request.method == 'POST':
        form = BandaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musicblog:listar_bandas')
    else:
        form = BandaForm()
    return render(request, 'musicblog/banda_crear.html', {'form':form})

def actualizar_banda(request, id):
    banda = get_object_or_404(Banda, id=id)

    if request.method == 'POST':
        form = BandaForm(request.POST, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('musicblog:listar_bandas')
    else:
        form = BandaForm(instance=banda)
        contexto = {'form':form}
    return render(request, 'musicblog/banda_crear.html', contexto)

def eliminar_banda(request, id):
    banda = get_object_or_404(Banda,id=id)
    if request.method == 'POST':
        banda.delete()
        return redirect('musicblog:listar_bandas')
    contexto = {'banda':banda}
    return render(request, 'musicblog/banda_eliminar.html',contexto)

### FIN Vistas de bandas ###

### INICIO Vistas de Discos ###

def listar_discos(request):
    discos = Disco.objects.all()
    return render(request, 'musicblog/disco_listar.html', {'discos':discos})

def crear_disco(request):
    if request.method == 'POST':
        form = DiscoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musicblog:listar_discos')
    else:
        form = DiscoForm()
    return render(request, 'musicblog/disco_crear.html', {'form':form})

def actualizar_disco(request, id):
    disco = get_object_or_404(Disco, id=id)

    if request.method == 'POST':
        form = DiscoForm(request.POST, instance=disco)
        if form.is_valid():
            form.save()
            return redirect('musicblog:listar_discos')
    else:
        form = DiscoForm(instance=disco)
        contexto = {'form':form}
    return render(request, 'musicblog/disco_crear.html', contexto)

def eliminar_disco(request, id):
    disco = get_object_or_404(Disco,id=id)
    if request.method == 'POST':
        disco.delete()
        return redirect('musicblog:listar_discos')
    contexto = {'disco':disco}
    return render(request, 'musicblog/disco_eliminar.html',contexto)

### FIN Vistas de Discos ###


### INICIO Vistas de Canciones ###

def listar_canciones(request):
    canciones = Cancion.objects.all()
    return render(request, 'musicblog/cancion_listar.html', {'canciones':canciones})

def crear_cancion(request):
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musicblog:listar_canciones')
    else:
        form = CancionForm()
    return render(request, 'musicblog/cancion_crear.html', {'form':form})

def actualizar_cancion(request, id):
    cancion = get_object_or_404(Cancion, id=id)

    if request.method == 'POST':
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            form.save()
            return redirect('musicblog:listar_canciones')
    else:
        form = CancionForm(instance=cancion)
        contexto = {'form':form}
    return render(request, 'musicblog/cancion_crear.html', contexto)

def eliminar_cancion(request, id):
    cancion = get_object_or_404(Cancion,id=id)
    if request.method == 'POST':
        cancion.delete()
        return redirect('musicblog:listar_canciones')
    contexto = {'cancion':cancion}
    return render(request, 'musicblog/cancion_eliminar.html',contexto)

### FIN Vistas de Canciones ###