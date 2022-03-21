from dataclasses import field
from email.mime import image
import imp
from select import select
from rest_framework import serializers
from .models import All_cakes,Occation


class All_cakesSerializer(serializers.ModelSerializer):
    
    occation_name = serializers.ReadOnlyField(source='occation.name')

    class Meta:
        model = All_cakes
        fields = '__all__'

    def get_photo_url(self, profile):
        request = self.context.get('request')
        photo_url = profile.image.url
        return request.build_absolute_uri(photo_url)
    

class OccationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occation
        fields = '__all__'