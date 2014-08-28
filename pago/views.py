from django.shortcuts import render
from producto.models import Pedido
from pago.models import ComprobantePago
from django.http import HttpResponse
from utilitario.forms import ImageUploadForm
from utilitario.models import Imagen
from membresia.models import Membresia
# Create your views here.

def datosPagoView(request):
	p = request.GET.get('pedido', 0)
	p = int(p)
	pedido = Pedido.objects.filter(serial = p )
	if(len(pedido)):
		total_pago = pedido[0].cantidad * pedido[0].producto.precio
		c = ComprobantePago.objects.filter(pedido = pedido[0])
		return render(request, 'pago/datospagoview.html', {'pedido' : pedido[0], 'total_pago':total_pago})
	return render(request, 'pago/datospagoview.html')

def subirRecibo(request):
	if request.method == 'POST':
		p = request.POST.get("pedido", " ")
		form = ImageUploadForm(request.POST, request.FILES)
		membresia = Membresia.objects.filter(user = request.user)
		

		if form.is_valid():			
			i = Imagen()
			i.imagen = form.cleaned_data['recibo']
			i.proposito = "recibo de compra"
			i.propietario = request.user.username
			i.save()

			pedido = Pedido.objects.get(pk = p)
			
			if(pedido.comprobante_pago):
				c = pedido.comprobante_pago
				c.imagen = i
				c.save()
				
				if(len(membresia)):
					return render(request, "main/principalview.html", {"mensaje":"Recibo subido con exito", "membresia":membresia[0]})
				form = ImageUploadForm()
				return render(request, "main/principalview.html", {"mensaje":"Recibo subido con exito, su pedido sera valido cuando cancele su membresia", "form":form})
			else:

				comprobante = ComprobantePago()				
				comprobante.imagen = i
				comprobante.save()
				pedido.comprobante_pago = comprobante
				pedido.save()

				if(len(membresia)):
					return render(request, "main/principalview.html", {"mensaje":"Recibo subido con exito", "membresia":membresia[0]})
				form = ImageUploadForm()
				return render(request, "main/principalview.html", {"mensaje":"Recibo subido con exito, su pedido sera valido cuando cancele su membresia", "form":form})
		#print("formulario invalido")
		if(len(membresia)):
			return render(request, "main/principalview.html", {"mensaje":"Archivo invalido", "membresia":membresia[0]})
		form = ImageUploadForm()
		return render(request, "main/principalview.html", {"mensaje":"Archivo invalido", "form":form})

def verHistorial(request):
	p = Pedido.objects.filter(usuario = request.user ).exclude(estado = "solicitado")
	#return HttpResponse(p)
	return render(request, "producto/historialcompraview.html", {"pedidos": p})
