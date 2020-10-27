from rest_framework import serializers

from location.serializers import CaseLocationOutputSerializer
from patient.serializers import PatientSerializer
from virus.serializers import VirusSerializer
from .models import Case


class CaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    confirmed_date = serializers.DateField()
    origin = serializers.CharField()

    patient = PatientSerializer()
    virus = VirusSerializer()

    case_locations = CaseLocationOutputSerializer(many=True)

    class Meta:
        model = Case
        fields = ("id", "confirmed_date", "origin", "patient", "virus", "case_locations")
