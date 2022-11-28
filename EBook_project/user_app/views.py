from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RegistrationSerializer
# Create your views here.


@api_view(['POST',])
def regsitration_view(request):
    if request.method=='POST':
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'key': 'value'}, status=status.HTTP_200_OK)
