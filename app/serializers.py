from rest_framework import serializers
from .models import *


class SchoolSerializer(serializers.Serializer):
    Email=serializers.CharField(required=True, error_messages={"error_message":"email is required"})
    Name = serializers.CharField(required=True,error_messages={"required":"Name is required"})
    City = serializers.CharField(required=True,error_messages={"required":"City is required"})
    Pincode = serializers.IntegerField(required=True,error_messages={"Pincode":"Pincode is required"})
    Password = serializers.CharField(required=True,error_messages={"required":"Password is required"})

class StudentsSerializer(serializers.Serializer):
    Name = serializers.CharField(required=True, error_messages={"required":"Name is required"})
    Grade = serializers.CharField(required=True, error_messages={"required":"Name is required"})
    Username = serializers.CharField(required=True, error_messages={"required":"Name is required"})
    Password = serializers.CharField(required=True, error_messages={"required":"Name is required"})


class SchoolLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, error_messages={"required":"email is required"})
    password = serializers.CharField(required=True,error_messages={"required":"password is required"})

class VerifySerializer(serializers.Serializer):
    email = serializers.CharField(required=True, error_messages={"required":"email is required"})
    otp = serializers.IntegerField(required=True, error_messages={"required":"OTP is required"})