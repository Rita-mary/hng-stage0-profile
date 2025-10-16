from django.shortcuts import render
from datetime import datetime, timezone
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
import requests 
from django.conf import settings
from rest_framework import status

logger = logging.getLogger(__name__)




class GetMyProfile(APIView):

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
