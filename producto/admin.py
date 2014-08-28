from django.contrib import admin
from producto.models import Producto, MetodoEnvio, Categoria, Pedido
# Register your models here.

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(MetodoEnvio)
admin.site.register(Pedido)