from django.shortcuts import render
from .models import Impacto
from .models import Depoimento


def index(request):
    contexto = {
        "impacto": Impacto.objects.first(),
        "depoimentos" : Depoimento.objects.all()
    }
    return render(request, "ampara/index.html",contexto)
