from django.db import models
from django.contrib.auth.models import User

from utilitario.models import Imagen
# Create your models here.

class ComprobantePago(models.Model):	
	serial = models.AutoField(primary_key=True)
	imagen = models.ForeignKey(Imagen)

	def image_img(self):
		if self.imagen:
			return u'<img src="%s" />' % self.imagen.url
		else:
			return '(Sin imagen)'
			imagen.short_description = 'Thumb'
			imagen.allow_tags = True

	def __unicode__(self):
		return str(self.serial)