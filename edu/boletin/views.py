from django.shortcuts import render
from .forms import RegForm
from .models import Registrado
# Create your views here.

def inicio(request):
    form = RegForm(request.POST or None)
    titulo = "Hola desconocido"
    if request.user.is_authenticated():
        titulo = "Bienvenido %s" %(request.user)
    #print (dir(form))
    if form.is_valid():
        form_data = form.cleaned_data
        abc = form_data.get("email")
        abc2 = form_data.get("nombre")
        obj = Registrado.objects.create(email=abc, nombre=abc2)

        #otra forma de insertar en la BD
#        obj = Registrado()
#        obj.email = abc
#        obj.save()

    context = {
        "titulo" : titulo,
        "el_form" : form,
    }
    return render(request,"inicio.html",context)
