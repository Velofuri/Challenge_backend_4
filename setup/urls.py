from django.contrib import admin
from django.urls import path, include
from financas.views import ReceitaViewSet, DespesaViewSet, ReceitasPorMes, DespesasPorMes
from rest_framework import routers

router = routers.DefaultRouter()
router.register('receita', ReceitaViewSet, basename='Receitas')
router.register('despesa', DespesaViewSet, basename='Despesas')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('receita/<int:ano>/<int:mes>', ReceitasPorMes.as_view()),
    path('despesa/<int:ano>/<int:mes>', DespesasPorMes.as_view())
]
