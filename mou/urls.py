from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blackdog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.indexView'),
	url(r'^login/$', 'autenticacion.views.loginView'),
	url(r'^login/create/user$', 'usuario.views.createUser'),      
	url(r'^login/error/$', 'autenticacion.views.errorview'),  
	url(r'^autenticacion/valida/$', 'autenticacion.views.sucessfullview'),

    #url referido
    url(r'^referido/referir/$', 'referido.views.referirForm'),
    url(r'^referido/enviar/invitacion$', 'referido.views.enviarInvitacion'),
    url(r'^referido/ver/referidos$', 'referido.views.verReferidos'),


    #productos
    url(r'^productos/ver/categorias$', 'producto.views.categoriasView'),
    url(r'^productos/ver/$', 'producto.views.productosView'),
    url(r'^productos/solicitar/pedido$', 'producto.views.solicitarPedido'),
    url(r'^productos/ver/pedidos$', 'producto.views.pedidosView'),

    #url notificaciones
    url(r'^notificaciones/pendientes/$', 'notificaciones.views.pendientesView'),
    url(r'^notificaciones/todas/$', 'notificaciones.views.todasView'),

    #usuario
    url(r'^usuario/perfil/$', 'usuario.views.perfilView'),
    url(r'^usuario/editarperfil/$', 'usuario.views.editarperfilForm'),
    url(r'^usuario/actualizar/$', 'usuario.views.actualizarPerfil'),
    url(r'^usuario/recuperar/password$', 'usuario.views.recuperarPassword'),

    #pagos
    url(r'^pago/ver/datos$', 'pago.views.datosPagoView'),
    url(r'^pago/subir/recibo$', 'pago.views.subirRecibo'),
    url(r'^pago/ver/historial$', 'pago.views.verHistorial'),

    #membresia
    url(r'^membresia/subir/recibo$', 'membresia.views.subirRecibo'),






    url(r'^admin/', include(admin.site.urls)),
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))