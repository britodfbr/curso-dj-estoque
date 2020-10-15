from django.contrib import admin
# Register your models here.
from .models import Produto

#  # Primeira forma para registrar o produto
# admin.site.register(Produto)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = '__str__', 'importado', 'ncm', 'preco', 'estoque', 'estoque_minimo',
    search_fields = 'produto',
    list_filter = 'importado',
