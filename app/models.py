from django.db import models


class Setor(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Setores'

class Funcao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    setor = models.ForeignKey('Setor', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Função"
        verbose_name_plural = "Funções"

class Funcionario(models.Model):
    nome = models.CharField(max_length=125)
    endereco = models.CharField(max_length=125)
    idade = models.IntegerField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    salario = models.FloatField("Salário")
    funcao = models.ForeignKey('Funcao', verbose_name='Função', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
