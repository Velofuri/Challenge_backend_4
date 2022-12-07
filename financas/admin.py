from django.contrib import admin
from financas.models import Receita, Despesa

class Receitas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'data', 'valor')
    list_display_links = ('id', 'descricao')
    list_per_page = 20

admin.site.register(Receita, Receitas)

class Despesas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'data', 'valor')
    list_display_links = ('id', 'descricao')
    list_per_page = 20

admin.site.register(Despesa, Despesas)