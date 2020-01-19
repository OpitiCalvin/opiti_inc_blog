from rest_framework import serializers
from opiti_blog.models import Contact, Location

class ContactSerializer(serializers.Serializer):
	r"""
	"""

	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True, allow_blank=False, max_length=50)
	email = serializers.EmailField(required=True, allow_blank=False, max_length=50)
	phone = serializers.CharField(required=False, allow_blank=True, max_length=15)
	# city = serializers.CharField(required=False, allow_blank=True, max_length=25)
	country = serializers.CharField(required=True, allow_blank=False, max_length=25)
	subject = serializers.CharField(required=True, allow_blank=False, max_length=30)
	message = serializers.CharField(required=True, allow_blank=False, max_length=300)

	def create(self,  validated_data):
		r"""
		Create and return a new client instance, given validated data.

		"""

		return Contact.objects.create(**validated_data)

	def update(self, instance, validated_data):
		r"""
		Update and return an existing Client instance, given validated data.

		"""

		instance.name = validated_data.get('name', instance.name)
		instance.email = validated_data.get('email', instance.email)
		instance.phone = validated_data.get('phone', instance.phone)
		# instance.city = validated_data.get('city', instance.city)
		instance.country = validated_data.get('country', instance.country)
		instance.subject = validated_data.get('subject', instance.subject)
		instance.message = validated_data.get('message', instance.message)

		instance.save()

		return instance	

class LocationSerializer(serializers.Serializer):
	r"""
	"""

	id = serializers.IntegerField(read_only=True)
	resp_id = serializers.IntegerField(required=True)
	latitude = serializers.FloatField(required=True)
	longitude = serializers.FloatField(required=True)
	accuracy = serializers.FloatField(required=False)

	def create(self,  validated_data):
		r"""
		Create and return a new client instance, given validated data.

		"""

		return Location.objects.create(**validated_data)