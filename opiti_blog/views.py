from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework.views import APIView
from rest_framework.response import Response
from opiti_blog.models import Contact
from opiti_blog.serializers import ContactSerializer

# Create your views here.
class ListContacts(APIView):
	def get(self, request, format=None):
		r"""
		"""

		contacts = Contact.objects.all()
		serializer = ContactSerializer(contacts, many = True)
		return Response(serializer.data)

	def post(self, request, format=None):
		r"""
		"""

		data = JSONParser().parse(request)
		serializer = ContactSerializer(data = data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=200)
		return JsonResponse(serializer.errors, status=400)

class ContactDetail(APIView):
	def get_object(self, pk, format=None):
		r"""
		"""

		try:
			return Contact.objects.get(pk)
		except Contact.DoesNotExist:
			return HttpResponse(status=404)

	def get(self, request, pk, format=None):
		r"""
		"""

		contact = self.get_object(pk)
		serializer = ContactSerializer(contact)
		return Response([serializer.data])

	def put(self, request, pk, format=None):
		r"""
		"""

		contact = self.get_object(pk)
		data = JSONParser().parse(request)
		serializer = ContactSerializer(contact, data = data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	def delete(self, request, pk, format=None):
		r"""
		"""

		contact = self.get_object(pk)
		contact.delete()
		return HttpResponse(status=201)