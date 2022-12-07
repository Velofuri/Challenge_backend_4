from django.db import models

class Receita(models.Model):
    descricao = models.CharField(max_length=100, blank=False, null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    data = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.descricao

class Despesa(models.Model):
    descricao = models.CharField(max_length=100, blank=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    data = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.descricao
