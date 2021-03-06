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

class Location(models.Model):
	r"""
	A db model used with Wits ACMS project to get locations of their \n
	respondents or health facilities they visited.

	"""

	resp_id = models.CharField(max_length=15, blank=False)
	phone = models.CharField(max_length=15, blank=True)
	latitude = models.FloatField(null=False, blank=False)
	longitude = models.FloatField(null=False, blank=False)
	terms_accepted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "Lat: {:f}; Lng: {:f}".format(self.latitude, self.longitude)
