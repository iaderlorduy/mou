from django.shortcuts import render
from referido.models import PosibleReferido
from usuario.models import Perfil
from django.http import HttpResponse
from notificaciones.models import Notificaciones
from producto.models import Pedido
from datetime import datetime
from membresia.models import Membresia
from utilitario.forms import ImageUploadForm
# Create your views here.

def indexView(request):
	if request.session.get('autenticado', 0) == 0:
		return render(request, 'autenticacion/loginview.html', { })

	if request.session.get('autenticado', 0) == 1:
		pedido = Pedido.objects.filter(usuario = request.user, estado = 'confirmando')
		membresia = Membresia.objects.filter(user = request.user)
		for nu in pedido:
			n =  Notificaciones()
			n.receptor = request.user
			n.estado = False
			n.fecha = datetime.now()
			n.mensaje = nu.estado
			n.emisor = nu.producto.nombre
			n.save()
		notificaciones = Notificaciones.objects.filter( receptor = request.user, estado = False).order_by('fecha')[:4]
		allNotificaciones = Notificaciones.objects.filter( receptor = request.user, estado = False)
		n_notificaciones = len(allNotificaciones)
		p_referidos = PosibleReferido.objects.filter ( auspiciador =  request.user.username )
		#perfil = Perfil.objects.filter( user = request.user)[0]
		posibleReferido = PosibleReferido.objects.filter(correo = request.user.email )
		#return HttpResponse(posibleReferido[0].auspiciador)
		

		#if perfil.auspiciador == '':
			#return HttpResponse('vacio')
		if (len(posibleReferido)):
			p_auspiciador = posibleReferido[0].auspiciador
			if(len(membresia)):
				return render (request, 'main/principalview.html', { 'p_referidos' : p_referidos, 'p_auspiciador': p_auspiciador, 'u_nombre' : request.user.username, 'notificaciones': notificaciones, 'n_notificaciones':n_notificaciones, "membresia":membresia[0]})
			form = ImageUploadForm()
			return render (request, 'main/principalview.html', { 'p_referidos' : p_referidos, 'p_auspiciador': p_auspiciador, 'u_nombre' : request.user.username, 'notificaciones': notificaciones, 'n_notificaciones':n_notificaciones, "form":form})	
		else:
			if(len(membresia)):
				return render (request, 'main/principalview.html', { 'p_referidos' : p_referidos, 'u_nombre' : request.user.username, 'notificaciones': notificaciones, 'n_notificaciones':n_notificaciones, "membresia":membresia[0]})
			form = ImageUploadForm()
			return render (request, 'main/principalview.html', { 'p_referidos' : p_referidos, 'u_nombre' : request.user.username, 'notificaciones': notificaciones, 'n_notificaciones':n_notificaciones,  "form":form})



