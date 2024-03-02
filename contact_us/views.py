from django.shortcuts import render
from rest_framework import viewsets
# from .models import ContactUs
# from contact_us.models import ContactUs
# from contact_us.serializers import ContactUsSerializer
from . import models
from . import serializers
# Create your views here.

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer
