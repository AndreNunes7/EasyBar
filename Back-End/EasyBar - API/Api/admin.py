from django.contrib import admin
from .models import *

@admin.register(Usuarios)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'cargo', 'is_active', 'is_staff']
    search_fields = ('username', 'cargo', 'email')
    list_filter = ['cargo', 'is_active']
    ordering = ['username']
    
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'categoria')
    search_fields = ('nome', 'categoria', 'estoque') 
    list_filter = ['categoria']  
    ordering = ['nome']  

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'capacidade', 'status')
    list_filter = ('status',)
    ordering = ['numero']  

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'valor_total', 'data')
    search_fields = ['produto__nome']
    list_filter = ['data']  
    ordering = ['-data']  

@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data', 'categoria')
    search_fields = ('descricao', 'categoria')
    list_filter = ['categoria', 'data']  
    ordering = ['data']  

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('comanda', 'metodo_pagamento', 'valor_pago', 'data_pagamento')
    list_filter = ['metodo_pagamento', 'data_pagamento']  
    ordering = ['-data_pagamento']  

@admin.register(LogAcao)
class LogAcaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'acao', 'data_acao')  
    list_filter = ['data_acao', 'usuario']  
    ordering = ['-data_acao']