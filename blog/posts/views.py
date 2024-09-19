from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 
from django.template import loader


def index(request):
    return HttpResponse("Hola mundo")

def inicio(request):
    template = loader.get_template("inicio.html")
    return HttpResponse(template.render())

def post_id(request, id_post):
    response = "La persona con id: es %s"
    return HttpResponse (response % id_post)

def post_list(request):
    post_list=Post.objects.all()
    return HttpResponse(post_list)

def post_template(request):
    post_list = Post.objects.all()
    template = loader.get_template("post_templates.html")
    context = {"post_list": post_list,}
    return HttpResponse(template.render(context, request))
