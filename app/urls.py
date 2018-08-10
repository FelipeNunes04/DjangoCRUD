from django.urls import path
from .views import Home, FuncionariosList

urlpatterns = [
   path('', Home.as_view(), name='home'),
   path('listar-funcionarios/', FuncionariosList.as_view(), name="listar-funcionarios" )
]