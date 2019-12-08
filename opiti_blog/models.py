from django.db import models

# Create your models here.

class Contact(models.Model):
	r"""
	"""
	
	name = models.CharField('Names', max_length= 50)
	email = models.EmailField('E-Mail')
	phone = models.CharField('Phone Contact', max_length=15, blank=True)
	# city = models.CharField('City', max_length=25, blank=True)
	country = models.CharField('Country', max_length=25, blank=True)
	subject = models.CharField('Subject', max_length=30)
	message = models.TextField('Message')

	def __str__(self):
		return self.name
