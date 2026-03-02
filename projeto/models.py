from django.db import models


class Tarefa(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(blank=True, null=True)
    create = models.DateField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    finished = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo
