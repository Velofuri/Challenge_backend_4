from rest_framework.test import APITestCase
from financas.models import Despesa
from django.urls import reverse
from rest_framework import status

class DespesaTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Despesas-list')
        self.despesa_1 = Despesa.objects.create(
            descricao='DESPESA_1', valor='12000', data='2022-12-17', categoria='outras'
        )
        self.despesa_2 = Despesa.objects.create(
            descricao='DESPESA_2', valor='2000', data='2022-12-10', categoria='alimentacao'
        )

    def test_requisicao_get_para_listar_despesas(self):
        '''Teste para verificar a requisição GET para listar todas as Despesas'''
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_registrar_despesa(self):
        """Teste para verificar a requisição POST para registrar uma despesa"""
        data = {
            'descricao':'TESTE3',
            'valor':'5.00',
            'data':'2022-12-17',
            'categoria':'educacao'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_atualizar_despesa(self):
        """Teste para verificar a requisição PUT para atualizar uma despesa"""
        data = {
            'descricao':'TESTE3',
            'valor':'5000.00',
            'data':'2022-12-17',
            'descricao':'lazer'
        }
        response = self.client.put('/despesas/2/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete_para_deletar_uma_despesa(self):
        """Teste para verificar a requisição DELETE para deletar uma despesa"""
        response = self.client.delete('/despesas/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)