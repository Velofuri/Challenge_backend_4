from rest_framework.test import APITestCase
from financas.models import Receita
from django.urls import reverse
from rest_framework import status

class ReceitaTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Receitas-list')
        self.receita_1 = Receita.objects.create(
            descricao='TESTE1', valor='15.000', data='2022-12-17'
        )
        self.receita_2 = Receita.objects.create(
            descricao='TESTE2', valor='9.000', data='2022-12-15'
        )

    def test_requisicao_get_para_listar_receitas(self):
        '''Teste para verificar a requisição GET para listar todas as Receitas'''
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_registrar_receitas(self):
        """Teste para verificar a requisição POST para registrar uma receita"""
        data = {
            'descricao':'TESTE3',
            'valor':'5.00',
            'data':'2022-12-17'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_atualizar_receita(self):
        """Teste para verificar a requisição PUT para atualizar uma receita"""
        data = {
            'descricao':'TESTE2',
            'valor':'5000.00',
            'data':'2022-12-17'
        }
        response = self.client.put('/receitas/2/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete_para_deletar_uma_receita(self):
        """Teste para verificar a requisição DELETE para deletar uma receita"""
        response = self.client.delete('/receitas/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)