from django.shortcuts import render

from .models import Funcionario

from django.views.generic import TemplateView
from django.views.generic.list import ListView


class Home(TemplateView):
	template_name = "index.html"

class FuncionariosList(ListView):
    template_name = "funcionario/listar.html"

    def get_queryset(self):
        try:
            maior = self.request.GET["maior"]
            maior = float(maior)
            funcionarios = [funcionario for funcionario in Funcionario.objects.all() if funcionario.salario>maior]
        except Exception as e:
            print(e)
            funcionarios = Funcionario.objects.all()
                    
        return funcionarios
