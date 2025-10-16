from django.urls import path 
from .views import GetMyProfile

urlpatterns = [
    path('me/', GetMyProfile.as_view(), name="my-profile"),
]