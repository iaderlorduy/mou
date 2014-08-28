from django.db import models
from django.contrib.auth.models import User
from utilitario.models import Imagen

# Create your models here.
class Membresia(models.Model):
	solicitado = 'solicitado'
	confirmado = 'confirmado'
	

	estados = (
        (solicitado, 'solicitado'),
        (confirmado, 'confirmado'),
        
    )

	user = models.ForeignKey(User)
	estado = models.CharField(max_length = 20, choices=estados,
                                      default=solicitado)

	imagen = models.ForeignKey(Imagen)

	def __unicode__(self):
		return self.user.username
