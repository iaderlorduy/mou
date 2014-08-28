from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
	user = models.ForeignKey(User)
	auspiciador = models.CharField( max_length = 20)
	direccion = models.CharField( max_length = 50, blank = True)
	edad = models.IntegerField(blank = True)
	fechaingreso = models.DateField(auto_now = True)
	imagen = models.ImageField( upload_to = 'perfil', blank = True)

	def __unicode__(self):
		return self.user.username