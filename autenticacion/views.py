from django.shortcuts import render
from django.contrib.auth import authenticate, login
from autenticacion.forms import userLoginForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from usuario.models import Perfil
from correo.views import sendMail
from django.http import HttpResponse
# Create your views here.
def loginView(request):
	if request.method == 'POST':
		usuario = request.POST.get('user', 0)
		password = request.POST.get('password', 0)
		if usuario and password:			
			user = authenticate(username=usuario, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					request.session['autenticado'] = 1
					return redirect('/')
			else:
				request.session['error'] = 'Usuario Invalido'
				return render(request, 'autenticacion/loginview.html', { 'mensaje': 'Usuario Invalido'})
		else:
				request.session['error'] = 'Formulario Invalido'
				return render(request, 'autenticacion/loginview.html', { 'mensaje': 'Formulario Invalido'})
	else:
		
		return render(request, 'autenticacion/loginview.html', { })

def sucessfullview(request):
	return render(request, 'autenticacion/sucesfullview.html', )

def errorview(request):
	return render(request, 'autenticacion/errorview.html', {'mensaje':request.session.get('error', False)})





