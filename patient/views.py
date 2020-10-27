from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PatientSerializer
from .models import Patient
from rest_framework import status


@api_view(['GET', 'POST'])
def patient_list(request):
    if request.method == 'GET':
        patient = Patient.objects.all()
        serializer = PatientSerializer(patient, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


@api_view(['GET', 'DELETE'])
def patient_detail(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)

        return Response(serializer.data)

    elif request.method == 'DELETE':
        patient.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)