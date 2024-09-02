import datetime
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EmailAccess
from .serializers import EmailAccessSerializer

@api_view(['POST'])
def add_email(request):
    serializer = EmailAccessSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def check_email(request, email):
#     try:
#         email_access = EmailAccess.objects.get(email=email)
#         exists = True
#     except EmailAccess.DoesNotExist:
#         exists = False
#     return Response({'exists': exists, }, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_email(request, email):
    try:
        email_access = EmailAccess.objects.get(email=email)
    except EmailAccess.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  
    email_access.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


from django.utils import timezone

@api_view(['GET'])
def check_email(request, email):
    try:
        email_access = EmailAccess.objects.get(email=email)
        current_date = timezone.now().date()
        # Convert expiry_date to date for comparison
        if email_access.expiry_date and email_access.expiry_date.date() < current_date:
            return Response({'exists': False, 'detail': 'Email access has expired.'}, status=status.HTTP_403_FORBIDDEN)
        exists = True
    except EmailAccess.DoesNotExist:
        exists = False

    return Response({'exists': exists}, status=status.HTTP_200_OK)