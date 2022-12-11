from rest_framework import viewsets, filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response
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

class ResumoPorMes(APIView):
    def get(self, request, ano, mes):
        ano = self.kwargs['ano']
        mes = self.kwargs['mes']
        total_receitas = self.total_receitas(ano, mes)
        total_despesas = self.total_despesas(ano, mes)
        saldo = total_receitas - total_despesas
        total_gasto_por_categoria = self.total_gasto_por_categoria(ano, mes)
        return Response(data={
            'total_receitas': total_receitas,
            'total_despesas': total_despesas,
            'saldo': saldo,
            'total_gasto_por_categoria': total_gasto_por_categoria
        })

    def total_receitas(self, ano, mes):
        receitas = Receita.objects.filter(data__year=ano, data__month=mes)
        valor = 0
        for receita in receitas:
            valor += receita.valor
        return valor

    def total_despesas(self, ano, mes):
        despesas = Despesa.objects.filter(data__year=ano, data__month=mes)
        valor = 0
        for despesa in despesas:
            valor += despesa.valor
        return valor

    def total_gasto_por_categoria(self, ano, mes):
        despesas = Despesa.objects.filter(data__year=ano, data__month=mes)
        categorias = self.get_dict_categorias()
        for item in despesas:
            categorias[item.categoria] += item.valor
        return categorias
    
    def get_dict_categorias(self):
        return {
            "alimentacao": 0,
            "saude": 0,
            "moradia": 0,
            "transporte": 0,
            "educacao": 0,
            "lazer": 0,
            "imprevisto": 0,
            "outras": 0
        }
