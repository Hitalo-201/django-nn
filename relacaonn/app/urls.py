from django.urls import path
from .views import *

urlpatterns = [
    path('listar_marca', listar_marca, name='listar_marca'),
    path('cadastrar_marca',cadastrar_marca, name='cadastrar_marca'),
    path('editar_marca/<int:pk>/', editar_marca, name='editar_marca'),
    path('deletar_marca/<int:pk>/', deletar_marca, name='deletar_marca'),
    path('marca/produto/<int:pk>/', listar_produto_marca, name='marca_produto'),


    path('listar_produto', listar_produto, name='listar_produto'),
    path('cadastrar_produto', cadastrar_produto, name='cadastrar_produto'),
    path('deletar_produto/<int:pk>/', deletar_produto, name='deletar_produto'),
    path('editar_produto/<int:pk>/', editar_produto, name='editar_produto'),
    path('perfil_produto/<int:pk>/', perfil_produto, name='perfil_produto'),


    path('listar_categoria', listar_categoria, name='listar_categoria'),
    path('cadastrar_categoria', cadastrar_categoria, name='cadastrar_categoria'),
    path('deletar_categoria/<int:pk>/', deletar_categoria, name='deletar_categoria'),
    path('editar_categoria/<int:pk>/', editar_categoria, name='editar_categoria'),
    path('categoria/produto/<int:pk>/', listar_produtos_categoria, name='categoria_produto'),
]
