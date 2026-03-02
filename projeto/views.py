from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth, messages
from .models import Tarefa


def index(request):
    return render(request, "index.html")


def lista_tarefa(request):
    tarefas = Tarefa.objects.all().order_by("-create")

    tarefa_editar = None

    if "editar" in request.GET:
        tarefa_id = request.GET.get("editar")
        try:
            tarefa_editar = Tarefa.objects.get(id=tarefa_id)
        except Tarefa.DoesNotExist:
            messages.error(request, "Tarefa não encontrada.")
            return redirect("tarefa")

    return render(
        request,
        "tarefa.html",
        {"tarefas": tarefas, "tarefa_editar": tarefa_editar},
    )


def salvar_tarefa(request):
    if request.method == "POST":
        tarefa_id = request.POST.get("tarefa_id")
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        deadline = request.POST.get("deadline")

        if tarefa_id:
            try:
                tarefa = Tarefa.objects.get(id=tarefa_id)
                tarefa.titulo = titulo
                tarefa.descricao = descricao
                tarefa.deadline = deadline
                tarefa.save()
                messages.success(request, "Tarefa atualizada!")
            except Tarefa.DoesNotExist:
                messages.error(request, "Tarefa não encontrada.")
        else:
            Tarefa.objects.create(titulo=titulo, descricao=descricao, deadline=deadline)
            messages.success(request, "Tarefa criada!")

    return redirect("tarefa")


def completar_tarefa(request, tarefa_id):
    from django.utils import timezone

    try:
        tarefa = Tarefa.objects.get(id=tarefa_id)
        tarefa.finished = timezone.now().date()
        tarefa.save()
        messages.success(request, "Tarefa concluída!")
    except Tarefa.DoesNotExist:
        messages.error(request, "Tarefa não encontrada.")

    return redirect("tarefa")


def excluir_tarefa(request, tarefa_id):
    try:
        tarefa = Tarefa.objects.get(id=tarefa_id)
        tarefa.delete()
        messages.success(request, "Tarefa excluída!")
    except Tarefa.DoesNotExist:
        messages.error(request, "Tarefa não encontrada.")

    return redirect("tarefa")