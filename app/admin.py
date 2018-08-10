from django.contrib import admin

from .models import Funcao, Setor, Funcionario


admin.site.register(Funcao)
admin.site.register(Setor)
admin.site.register(Funcionario)