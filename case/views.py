from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CaseSerializer
from .models import Case
from rest_framework import status


@api_view(['GET', 'POST'])
def case_list(request):
    if request.method == 'GET':
        case = Case.objects.all()
        serializer = CaseSerializer(case, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CaseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


@api_view(['GET', 'DELETE'])
def case_detail(request, pk):
    try:
        case = Case.objects.get(pk=pk)
    except Case.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CaseSerializer(case)

        return Response(serializer.data)

    elif request.method == 'DELETE':
        case.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)