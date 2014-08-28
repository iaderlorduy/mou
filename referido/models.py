from django.db import models

# Create your models here.

class PosibleReferido(models.Model):
	auspiciador = models.CharField( max_length = 20)
	nombre = models.CharField( max_length = 20)
	correo = models.EmailField(max_length=70, unique = True)
	estado = models.BooleanField ( default = False )

	def __unicode__(self):
		return self.nombre
