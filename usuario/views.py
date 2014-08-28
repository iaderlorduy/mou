from django.shortcuts import render
from django.contrib.auth import authenticate, login
from autenticacion.forms import userLoginForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from usuario.models import Perfil
from correo.views import sendMail
from django.http import HttpResponse
from referido.models import PosibleReferido
from correo.views import sendMail
import string
import random
# Create your views here.

def perfilView(request):
	#n_usuario = request.GET.get('perfilview','')
	#usuarioActual = User.objects.filter(username = 'iader')
	perfilactual = Perfil.objects.filter(user = request.user)
	return render(request, 'usuario/perfilview.html',{'perfilactual' : perfilactual[0]})


def createUser(request):
	usuario = request.POST.get('user', 0)
	password = request.POST.get('password', 0)
	mail = request.POST.get('mail', 0)
	direccion = request.POST.get('direccion', 0)
	edad = request.POST.get('edad', 0)
	imagen = request.POST.get('imagen', 0)
	if usuario and password and mail:	

		if User.objects.filter(email = mail):
			return render(request, 'autenticacion/loginview.html', { 'mensaje': 'Este usuario ya existe'})

		try:
			user = User.objects.create_user(usuario, mail, password)
			user.save()				

		except :
			return render(request, 'autenticacion/loginview.html', { 'mensaje': 'Este usuario ya existe'})

		try:
			sendMail(mail, 'Usuario Registrado', 'Su usuario ' + usuario+ 'ha sido creado con exito.')
		except:
			return render(request, 'autenticacion/loginview.html', { 'mensaje': 'Problema al enviar correo'})

		try:
			u = User.objects.filter(username = usuario)
			#return HttpResponse(u[0].email)
			p = Perfil()
			p.user = user
			p.direccion = direccion
			p.edad = edad
			p.imagen =	imagen
			p.save()

		except:
			return render(request, 'autenticacion/loginview.html', { 'mensaje': 'Problema al crear perfil'})

		request.session['autenticado'] = 1
		user = authenticate(username=usuario, password=password)
		login(request, user)

		posibleReferido = PosibleReferido.objects.filter(correo = request.user.email )
		
		if (len(posibleReferido)):
			p_auspiciador = posibleReferido[0].auspiciador
			posibleReferido[0].estado = True
			posibleReferido[0].save()
			
			
			
			return render (request, 'main/principalview.html', { 'p_auspiciador': p_auspiciador,'u_nombre' : p.user.username })
		return render (request, 'main/principalview.html', {'u_nombre' : p.user.username })
		
	else:
		request.session['error'] = 'Formulario Invalido'
		return render(request, 'autenticacion/loginview.html', { 'mensaje': 'Formulario invalido'})

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def recuperarPassword(request):
	mail = request.POST.get("mail", " ")
	#return HttpResponse(mail)
	usuario = User.objects.filter( email = mail)

	if (len(usuario)):
		new_pass = id_generator(5)
		usuario[0].set_password( new_pass)
		usuario[0].save()
		sendMail(mail, "recuperacion de password", "su password es: "+new_pass)
		#return HttpResponse(mail+ " enviado	")
		return render(request, "autenticacion/loginview.html", {"mensaje":"revise su correo"})
	else:
		#return HttpResponse("correo invalido")
		return render(request, "autenticacion/loginview.html", {"mensaje":"correo invalido"})

def editarperfilForm(request):
	perfil_aEditar = request.GET.get('perfil_aEditar')
	print perfil_aEditar
	perfilE = Perfil.objects.filter(pk = perfil_aEditar)
	return render(request, 'usuario/editarperfilform.html', {'perfilE': perfilE[0]})

def actualizarPerfil(request):
	nombre = request.POST.get('nombre')
	direccion = request.POST.get('direccion')
	edad = request.POST.get('edad')
	u_actualizar = User.objects.get(username = request.user.username)
	p_actualizar = Perfil.objects.get(user = u_actualizar)
	u_actualizar.username = nombre
	u_actualizar.save()
	#print u_actualizar.username
	#print p_actualizar.user.username
	p_actualizar.user = u_actualizar
	p_actualizar.direccion = direccion
	p_actualizar.edad = edad
	p_actualizar.save()


	return render(request, "usuario/actualizar.html")
