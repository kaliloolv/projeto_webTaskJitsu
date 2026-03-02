from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tarefa/", views.lista_tarefa, name="tarefa"),
    path("salvar/", views.salvar_tarefa, name="salvar_tarefa"),
    path("completar/<int:tarefa_id>/", views.completar_tarefa, name="completar_tarefa"),
    path("excluir/<int:tarefa_id>/", views.excluir_tarefa, name="excluir_tarefa"),
]
