from dataclasses import field
from email.mime import image
import imp
from select import select
from rest_framework import serializers
from .models import All_cakes,Occation



class OccationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occation
        fields = '__all__'





class All_cakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = All_cakes
        fields = '__all__'

    def get_photo_url(self, profile):
        request = self.context.get('request')
        photo_url = profile.image.url
        return request.build_absolute_uri(photo_url)

    def to_representation(self, instance):
        self.fields['occation'] =  OccationSerializer(read_only=True)
        return super().to_representation(instance)
    
