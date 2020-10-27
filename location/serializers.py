from rest_framework import serializers

from .models import Location, CaseLocation


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class CaseLocationOutputSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    date_from = serializers.DateField()
    date_to = serializers.DateField()
    category = serializers.CharField()

    location = LocationSerializer()

    class Meta:
        model = CaseLocation
        fields = '__all__'


class CaseLocationInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseLocation
        fields = '__all__'
