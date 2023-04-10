from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework import generics
from .serializers import *
from django.contrib.auth.hashers import make_password, check_password
import jwt
from django.http import JsonResponse
from django.core.mail import send_mail
import random
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
     return render(request,'index.html')    

# OTP Function

def gen_otp():
    otp = random.randint(1000,9999)
    return otp

# E-mail Function

def send_email_via(subject,message,email_from,to):
    recipient_list = [to, ]
    send_mail(subject,message,email_from,recipient_list)
    
# decode Token Function    

def check_auth(request):
    encoded = request.headers['Authorization']
    decoded = jwt.decode(encoded,"secret", algorithms=["HS256"])
    
    return True, decoded['School_id']

#School View start Here 

class SchoolGetView(generics.GenericAPIView):
    def get(self,request):
        sl = School.objects.all()
        serializers = SchoolSerializer(sl ,many=True)

        return Response(serializers.data)


class SchoolPostView(generics.GenericAPIView):
    def post(self,request):
        serializers=SchoolSerializer(data=request.data)
        if serializers.is_valid():
            if not School.objects.filter(Email = serializers.data['Email']):
                otp = gen_otp()
                send_email_via(subject="Your OTP mail", message=f"Your OTP is: {otp}", email_from="skunknown7991@gmail.com",to= serializers.data['Email'])
                School.objects.create(Email=serializers.data['Email'],Name=serializers.data['Name'],City=serializers.data['City'],Pincode=serializers.data['Pincode'],Password=make_password(serializers.data['Password']),Otp=otp)
                return Response(serializers.data)
            else:
                Response("email already present")
        else:
            return Response(serializers.errors)

class SchoolLoginView(generics.GenericAPIView):
    def post(self,request, *args, **kwargs):
        try:
            serializers=SchoolLoginSerializer(data=request.data)
            if serializers.is_valid():
                instance = School.objects.filter(Email = serializers.data['email'])
                # print("this is instance", instance)
                if instance:
                    # print(True)
                    if check_password(serializers.data['password'], instance[0].Password):
                        encoded = jwt.encode({'School_id':instance[0].id}, "secret", algorithm='HS256')
                        return JsonResponse({'token':encoded})
        except Exception as e:
            print(e)

class SchoolVerifyView(generics.GenericAPIView):
    def post(self,request):
        serializers = VerifySerializer(data=request.data)
        if serializers.is_valid():
            instance = School.objects.filter(Email = serializers.data['email'],Otp = serializers.data['otp'])
            if instance:
                return Response("Your verification is successfully")
            else:
                return Response("Your OTP does not match")
        
        else:
            return Response(serializers.errors)



# School View Ends Here 

#Students Views Start Here 

class StudentsGetView(generics.GenericAPIView):
    def get(self,requrest):
        stu=Students.objects.all()
        serializers=StudentsSerializer(stu,many=True)
        return Response(serializers.data)
    

class StudentsPostView(generics.GenericAPIView):
    def post(self,request):
        auth_status,school_id = check_auth(request)
        if auth_status:
            serializers=StudentsSerializer(data=request.data)
            if serializers.is_valid():
                Students.objects.create(School_name_id=school_id,Name=serializers.data['Name'],Grade=serializers.data['Grade'],Username=serializers.data['Username'],Password=serializers.data['Password'])
                # send_email_via()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
        else:
            return None

class SchoolStudentView(generics.GenericAPIView):
    def get(self,request):
        auth_status,school_id = check_auth(request)
        print(auth_status)
        if auth_status:
            instance = Students.objects.filter(School_name_id=school_id).values()
            # list_data = [entry for entry in instance]
            list_data = []
            for entry in instance:
                list_data.append(entry)

            # print(li)
            # print(instance)
            return JsonResponse({"data":list_data})
        else:
            return Response(instance.errors)        


# Students Views End Here



    


