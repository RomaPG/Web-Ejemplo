from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm

def index(request):
    context={}
    return render(request, 'pagina/index.html', context)


def Accesorios(request):
    context={}
    return render(request, 'pagina/Accesorios.html', context)

def Comidas(request):
    context={}
    return render(request, 'pagina/Comidas.html', context)

def Juguetes(request):
    context={}
    return render(request, 'pagina/Juguetes.html', context)

def Snacks(request):
    context={}
    return render(request, 'pagina/Snacks.html', context)

def Registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Ya se registró!')  # Mensaje de éxito
            return redirect('Accesorios')  # Redirige a la página de Accesorios o donde desees
    else:
        form = RegistroForm()
    
    return render(request, 'pagina/Registro.html', {'form': form})