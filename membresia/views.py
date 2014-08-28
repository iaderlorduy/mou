from django.shortcuts import render
from django.http import HttpResponse
from utilitario.forms import ImageUploadForm
from utilitario.models import Imagen
from membresia.models import Membresia
# Create your views here.


def subirRecibo(request):
	if request.method == 'POST':
		
		form = ImageUploadForm(request.POST, request.FILES)
		
		

		if form.is_valid():			
			i = Imagen()
			i.imagen = form.cleaned_data['recibo']
			i.proposito = "recibo de compra"
			i.propietario = request.user.username
			i.save()

			membresia = Membresia.objects.filter(user = request.user)
			
			if(len(membresia)):
				membresia.estado = "solicitado"
				membresia[0].imagen = i
				membresia[0].save()
				
				
				return render(request, "main/principalview.html", {"Mensaje":"Comprobante subido con exito", "membresia":membresia})
			else:

				membresia = Membresia()	
				membresia.user = request.user			
				membresia.imagen = i
				membresia.estado = "solicitado"
				membresia.save()
				
				return render(request, "main/principalview.html", {"Mensaje":"Comprobante subido con exito", "membresia":membresia})
		#print("formulario invalido")
		return HttpResponse("formlario invalido")
