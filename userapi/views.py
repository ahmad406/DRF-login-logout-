from django.utils.translation import to_locale
from rest_framework import authentication
from rest_framework import permissions
from userapi import models,serializer
from rest_framework import viewsets 
from rest_framework import response, serializers
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings





class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes =(TokenAuthentication,)





class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES