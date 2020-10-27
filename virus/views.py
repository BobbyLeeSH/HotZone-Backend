from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import VirusSerializer
from .models import Virus
from rest_framework import status


@api_view(['GET', 'POST'])
def virus_list(request):
    if request.method == 'GET':
        virus = Virus.objects.all()
        serializer = VirusSerializer(virus, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VirusSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


@api_view(['GET', 'DELETE'])
def virus_detail(request, pk):
    try:
        virus = Virus.objects.get(pk=pk)
    except Virus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VirusSerializer(virus)

        return Response(serializer.data)

    elif request.method == 'DELETE':
        virus.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)