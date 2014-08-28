from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Notificaciones(models.Model):
	receptor = models.ForeignKey(User)
	estado = models.BooleanField(default = True)
	fecha = models.DateField(blank=True)
	mensaje = models.TextField()
	emisor = models.TextField()


	def __unicode__(self):
		return self.receptor.username