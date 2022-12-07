from django.contrib import admin
from django.urls import path, include
from financas.views import ReceitaViewSet, DespesaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('receita', ReceitaViewSet, basename='Receitas')
router.register('despesa', DespesaViewSet, basename='Despesas')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls))
]
