# Django imports.
from django.db import transaction

from help_api.models import *

# Rest Framework imports.
from rest_framework import serializers
from help_api.api.serializers import *

class RegisterEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityModel
        fields = ['entity_name']

class RegisterAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = ['entity_id', 'lane', 'town', 
        'district', 'state', 'contact_phone', 
        'contact_alternate_phone', 'email']
    
    def validate(self, data):
        if data['contact_phone'] is None:
            raise serializers.ValidationError("Contact cannot be empty")
        
        elif data['lane'] is None | data['town'] is None:
            raise serializers.ValidationError("lane and town cannot be empty")
        
        return data

    
