from django.shortcuts import render
from producto.models import Categoria, Producto, Pedido, MetodoEnvio
from django.http import HttpResponse
from utilitario.forms import ImageUploadForm
# Create your views here.
def categoriasView(request):
	categorias = Categoria.objects.all()
	return render(request, 'producto/categoriasview.html', {'categorias' : categorias })

def productosView(request):
	c = request.GET.get('categoria', ' ')
	productos = Producto.objects.filter( categoria = c).order_by('pk')
	if (len(c)):
		return render(request, 'producto/productosview.html', {'productos' : productos })
	else:
		return render(request, 'producto/productosview.html')

def solicitarPedido(request):

	p = request.POST.get('producto', 0)
	metodo_envio = request.POST.get('metodo_envio', 0)
	cantidad = request.POST.get('cantidad', 0)
	producto = Producto.objects.filter( pk = p)
	pedido = Pedido()
	pedido.usuario = request.user
	pedido.producto = producto[0]
	envio = MetodoEnvio.objects.filter( pk = metodo_envio)
	pedido.metodo_envio = envio[0]	
	pedido.cantidad = cantidad
	pedido.save()

	pedidos = Pedido.objects.filter( usuario = request.user).order_by('-fecha')

	return render( request, 'producto/solicitudpedidoview.html' , {'pedidos': pedidos } )

def pedidosView(request):
	form = ImageUploadForm()
	pedidos = Pedido.objects.filter( usuario = request.user).order_by('-fecha')
	#return HttpResponse(pedidos[0].producto)
	return render( request, 'producto/pedidosview.html' , {'pedidos': pedidos, 'form':form })


