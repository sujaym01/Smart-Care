from rest_framework import serializers
# from .models import ContactUs
# from contact_us.models import ContactUs
from .import models
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = '__all__'