from django.urls import path
from projeto.views import index

urlpatterns = [
    path("", index, name="index"),


]
