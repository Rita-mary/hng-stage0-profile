from django.shortcuts import render
from datetime import datetime, timezone
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
import requests 
from django.conf import settings
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

logger = logging.getLogger(__name__)




class GetMyProfile(APIView):

    @swagger_auto_schema(
        operation_description="Get profile info and a random cat fact.",
        responses={
            200: openapi.Response(
                description="Successful Response",
                examples={
                    "application/json": {
                        "status": "success",
                        "user": {
                            "email": "amakomritamary322@gmail.com",
                            "name": "Rita-mary Ngozi Amakom",
                            "stack": "Python/Django/Django REST Framework"
                        },
                        "timestamp": "2025-10-16T14:00:00.000Z",
                        "fact": "Cats sleep for 70% of their lives."
                    }
                }
            )
        }
    )
    def get(self,request):
        timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        email = getattr(settings,'MY_EMAIL', 'alt - amakomritamary322@gmail.com')
        name = getattr(settings, 'MY_NAME', 'alt - Rita-mary Ngozi Amakom')
        stack = getattr(settings, 'MY_STACK', 'alt - python-django-djangorestframework')
        try:
            response = requests.get('https://catfact.ninja/fact', timeout=10)
            logger.info("Connected successfully to cat facts api.")
        except Exception as e:
            logger.exception("There was an error connecting to the cat facts api.")
            response = ''
        if response:
            fact = response.json().get('fact')
            logger.info("Cat fact successfully gotten")
        else:
            fact = "Sorry, we could not get facts from cat facts this time, try again."
            logger.info("No cat fact was found")

        data = {
            "status": "success",
            "user": {
            "email": email,
            "name": name,
            "stack": stack
            },
            "timestamp": timestamp,
            "fact": fact
            }
        return Response(data, status=status.HTTP_200_OK)
