from django.shortcuts import render, redirect
from .models import Jugador, Equipo

from .forms import EquipoForm

def home(request):
    equipos = Equipo.objects.all()
    return render(request,'teamapp/index.html',{'equipos': equipos})

def creaequipos(request):
    if request.method=='GET':
        form = EquipoForm()
        return render(request,'teamapp/crear_equipo.html',{"form": form})
    else:
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")



