from django.shortcuts import render
from notificaciones.models import Notificaciones


# Create your views here.
def pendientesView(request):
	p = request.GET.get('pendientesview','')
	notificaciones = Notificaciones.objects.filter( pk = p)
	for n in notificaciones:
		n.estado = True
		n.save()
	return render(request, 'notificaciones/pendientesview.html',{'notificaciones':notificaciones})

def todasView(request):	
	#notificaciones = Notificaciones.objects.all()
	notificaciones = Notificaciones.objects.filter( receptor = request.user).order_by('fecha')
	return render (request, 'notificaciones/todasview.html',{'notificaciones':notificaciones})

