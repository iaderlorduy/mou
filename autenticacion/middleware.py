from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse

class AutenticarMidleware():
	def process_request(self, request):
		path = request.get_full_path()

		#return HttpResponse(path)
		if path == "/logout":
			#return HttpResponse("Bandera 2")	
			
			logout(request)
			request.session['autenticado'] = 0
			return redirect('/')
		else:
			if  (not path == "/") and (not path == "/login/")and (not path == "/admin/") and (not path == "/login/error/") and (not path == "/login/create/user") and (not path == "/usuario/recuperar/password") :
				
				#formulario = userLoginForm()
				#return render(request, 'autenticacion/loginview.html', { 'path':request.get_full_path(), 'form': formulario })
				if not request.user.is_authenticated():
					request.session['error'] = 'Usuario sin permisos'
					return redirect('/login/error/')									