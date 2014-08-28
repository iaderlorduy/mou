from django.db import models
from django.contrib.auth.models import User
from pago.models import ComprobantePago
# Create your models here.


class MetodoEnvio(models.Model):
	nombre = models.CharField(max_length = 20)
	descripcion = models.TextField (max_length = 50)
	
	def __unicode__(self):
		return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length = 20)
	descripcion = models.TextField(max_length = 50)

	def __unicode__(self):
		return self.nombre


class Producto(models.Model):
	nombre = models.CharField( max_length = 20)
	descripcion  = models.TextField( max_length = 100)
	precio = models.IntegerField()
	imagen = models.ImageField( upload_to = 'productos')
	categoria = models.ForeignKey(Categoria)
	metodos_de_envio = models.ManyToManyField(MetodoEnvio)
	
	
	def __unicode__(self):
		return self.nombre

class Pedido(models.Model):
	solicitado = 'solicitado'
	confirmando = 'confirmando'
	enviado = 'enviado'
	camino = 'camino'
	entregado = 'entregado'

	estados = (
        (solicitado, 'solicitado'),
        (confirmando, 'confirmando'),
        (enviado, 'enviado'),
        (camino, 'camino'),
        (entregado, 'entregado'),
    )
	usuario = models.ForeignKey(User)
	serial = models.AutoField(primary_key=True)
	producto = models.ForeignKey(Producto)
	fecha = models.DateTimeField(  auto_now = True)
	metodo_envio = models.ForeignKey(MetodoEnvio)
	comentario = models.TextField(blank = True)
	estado = models.CharField(max_length = 20, choices=estados,
                                      default=solicitado)
	cantidad = models.IntegerField()
	comprobante_pago = models.ForeignKey(ComprobantePago, blank = True, null = True)
	def total(self):
		return 1

	def __unicode__(self):
		return str(self.serial)




