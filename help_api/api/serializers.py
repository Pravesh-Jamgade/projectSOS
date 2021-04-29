# Django imports.
from django.db import transaction

from help_api.models import *

# Rest Framework imports.
from rest_framework import serializers

class RegisterAddressSerializer(serializers.Serializer):
    pass

class RegisterEntitySerializer(serializers.Serializer):
    entity_name = models.CharField(max_length=50)
    lane = models.CharField(("lane"), max_length=250)
    town = models.CharField(("town"), max_length=300)
    district = models.CharField(
        ("district"), max_length=300
    )
    state = models.CharField(("state"), max_length=300)
    contact_phone = models.CharField(max_length=10)
    contact_alternate_phone = models.CharField(max_length=10)
    email = models.EmailField("email", null=True, blank=True)

    # def validate(self, data, *args, **kwargs):
    #     return super(RegisterEntitySerializer, self).validate(data, *args, **kwargs)
    
    def create(self, validated_data):
        entity = EntityModel.objects.create(**validated_data)
        return entity