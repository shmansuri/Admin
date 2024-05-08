from rest_framework import serializers
from .models import ContactPage
 
class mySerializer(serializers.Serializer):

    name= serializers.CharField(max_length=50)
    email= serializers.EmailField(max_length=100)
    phone= serializers.CharField(max_length=14)
    company= serializers.CharField(max_length=50)
    company_website= serializers.CharField(max_length=50)
    services= serializers.CharField(max_length=50)
    describe= serializers.CharField(max_length=500)
    term= serializers.BooleanField(default=False)

    # def update(self, instance, validated_data):
    #     instance.name=validated_data.get('name', instance.name)
    #     instance.email=validated_data.get('email', instance.email)
    #     instance.name=validated_data.get('name', instance.name)
    #     instance.name=validated_data.get('name', instance.name)
    #     instance.name=validated_data.get('name', instance.name)
    #     instance.name=validated_data.get('name', instance.name)
    #     instance.name=validated_data.get('name', instance.name)
