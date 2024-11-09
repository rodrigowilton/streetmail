from django.urls import path
from . import views

urlpatterns = [
    path("criar/", views.criar_apto, name="criar_apto"),
    path("adicionar/", views.criar_apto, name="adicionar_morador"),
    path("editar/<int:pk>/", views.editar_apto, name="editar_apto"),
    path("deletar/<int:pk>/", views.deletar_apto, name="deletar_apto"),
    path("", views.listar_aptos, name="listar_aptos"),
]
