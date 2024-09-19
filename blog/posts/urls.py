from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name = "home"),
        path("<int:id_post>", views.post_id, name="post_id"),
        path("post_list", views.post_list, name="post_list"),
        path("post_template", views.post_template, name="post_template"),
        path("inicio", views.inicio, name="inicio")
]