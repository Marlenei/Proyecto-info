from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioForm
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    template = loader.get_template("inicio.html")
    return HttpResponse(template.render())

def Usuario_created(request):

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()

    return render(request, 'registro.html', {
    'form':form,
    })
    