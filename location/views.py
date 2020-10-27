from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .serializers import LocationSerializer, CaseLocationInputSerializer, CaseLocationOutputSerializer
from .models import Location, CaseLocation
from rest_framework import status


@api_view(['GET', 'POST'])
def location_list(request):
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LocationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


@api_view(['GET', 'DELETE'])
def location_detail(request, pk):
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LocationSerializer(location)

        return Response(serializer.data)

    elif request.method == 'DELETE':
        location.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def location_search(request, place):
    res = requests.get('https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=' + place)
    if res.status_code == 200:
        # TODO. Handle multiple return values later
        ret = res.json()[0]

        location = Location.objects.filter(x_coord=ret['x']).filter(y_coord=ret['y'])
        if location.exists():
            print("location exists")
            serializer = LocationSerializer(location.first())
            return Response(serializer.data)
        else:
            location = Location(name=ret['nameEN'], address=ret['addressEN'], x_coord=ret['x'], y_coord=ret['y'])
            location.save()
            serializer = LocationSerializer(location)
            return Response(serializer.data)
    return Response('Geo Data API is not stable at the moment', status=status.HTTP_409_CONFLICT)


@api_view(['GET', 'POST'])
def case_location_list(request):
    if request.method == 'GET':
        case_location = CaseLocation.objects.all()
        serializer = CaseLocationOutputSerializer(case_location, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CaseLocationInputSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


@api_view(['GET', 'DELETE'])
def case_location_detail(request, pk):
    try:
        case_location = CaseLocation.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        print(case_location.case)
        print(case_location.location)
        serializer = CaseLocationOutputSerializer(case_location)

        return Response(serializer.data)

    elif request.method == 'DELETE':
        case_location.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
