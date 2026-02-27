from django.db import models


# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    create = models.DateField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    finished = models.DateField(null=True)
