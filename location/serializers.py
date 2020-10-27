from rest_framework import serializers

from .models import Location, CaseLocation


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class CaseLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseLocation
        fields = '__all__'
