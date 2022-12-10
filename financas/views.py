from rest_framework import viewsets, filters, generics
from financas.models import Receita, Despesa
from financas.serializers import ReceitaSerializer, DespesaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ReceitaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Receitas"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['descricao']
    search_fields = ['data', 'descricao']

class DespesaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Despesas"""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['descricao']
    search_fields = ['data', 'descricao']
    
class ReceitasPorMes(generics.ListAPIView):
    def get_queryset(self):
        ano = self.kwargs['ano']
        mes = self.kwargs['mes']
        queryset = Receita.objects.filter(data__year=ano, data__month=mes)
        return queryset
    serializer_class = ReceitaSerializer

class DespesasPorMes(generics.ListAPIView):
    def get_queryset(self):
        ano = self.kwargs['ano']
        mes = self.kwargs['mes']
        queryset = Despesa.objects.filter(data__year=ano, data__month=mes)
        return queryset
    serializer_class = DespesaSerializer