from django.shortcuts import render
from .forms import LoginForm
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    template = loader.get_template("inicio.html")
    return HttpResponse(template.render())

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, 
                                username=cd['username'],
                                password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Usuario autenticado')
                else:
                    return HttpResponse('Usuario inactivo')
            else:
                return HttpResponse('Usuario no encontrado')
    else:
        form = LoginForm()
    return render (request, 'account/login.html', {'form':form})



@login_required
def dashboard(request):
    return render(request, 'post_templates.html', {'post_templates':'post_templates'})