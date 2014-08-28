from django.db import models

# Create your models here.
class Imagen(models.Model):
	fecha  = models.DateTimeField(auto_now_add=True)
	imagen = models.FileField( upload_to = 'comprobantes', null=True, blank=True)
	propietario = models.CharField(max_length = 50)
	proposito = models.CharField(max_length = 50)
	def __unicode__(self):
		return self.imagen.url
