from rest_framework import viewsets
from financas.models import Receita, Despesa
from financas.serializers import ReceitaSerializer, DespesaSerializer

class ReceitaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Receitas"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

class DespesaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Despesas"""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer