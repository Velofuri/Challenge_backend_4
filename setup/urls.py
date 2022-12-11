from django.contrib import admin
from django.urls import path, include
from financas.views import ReceitaViewSet, DespesaViewSet, ReceitasPorMes, DespesasPorMes, ResumoPorMes
from rest_framework import routers

router = routers.DefaultRouter()
router.register('receitas', ReceitaViewSet, basename='Receitas')
router.register('despesas', DespesaViewSet, basename='Despesas')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('receita/<int:ano>/<int:mes>', ReceitasPorMes.as_view()),
    path('despesa/<int:ano>/<int:mes>', DespesasPorMes.as_view()),
    path('resumo/<int:ano>/<int:mes>', ResumoPorMes.as_view())
]
