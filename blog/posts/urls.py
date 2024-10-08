from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name = "home"),
        # path("<int:id_post>", views.post_id, name="post_id"),
        # path("post_list", views.post_list, name="post_list"),
        path("post_templates", views.post_templates, name="post_templates"),
        path("subir_post", views.subir_post , name="subir_post"),
        # path('misposteos', views..., name = 'misposteos'),
        path('<int:pk>/', views.post_id, name='post_detail' ),
        path('comentario/', views.Comentar_Noticia, name = 'comentar'),
        path('eliminar/<int:com_id>/', views.delete_comentario, name = 'delete_comentario'),

        
]