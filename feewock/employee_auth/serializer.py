from .models import Employees
from rest_framework.serializers import ModelSerializer
from django.conf import settings
from rest_framework import serializers
import random
from datetime import datetime , timedelta
from django.core.mail import send_mail
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags



class EmployeeSerializer(ModelSerializer):
    password1 = serializers.CharField(
        write_only = True,
        min_length = settings.MIN_PASSWORD_LENGTH,
        error_messages = {
            "min_length":"password must be longer than {} characters".format(
                settings.MIN_PASSWORD_LENGTH
            )
        }
    )

    password2 = serializers.CharField(
        write_only = True,
        min_length = settings.MIN_PASSWORD_LENGTH,
        error_messages = {
            "min_length":"password must be longer than {} characters".format(
                settings.MIN_PASSWORD_LENGTH
            )
        }
    )

    class Meta:
        model = Employees 
        fields = ['id','username','email','gender','phone_number','dob','address','city','state','type_of_work','adhar_number','images','bank_details','is_active','position','location','password1','password2','role']
    read_only_fields = ["id"]

    def validate(self , data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("passsword do not match")
        return data
    
    def create(self, validated_data):
        otp = random.randint(1000,9999)
        otp_expiry = datetime.now() + timedelta(minutes=2)

        position_data = validated_data.pop("position", None)
        employee = Employees(
            username=validated_data["username"],
            gender=validated_data["gender"],
            role = validated_data["role"],
            dob=validated_data["dob"],
            address=validated_data["address"],
            city=validated_data["city"],
            state=validated_data["state"],
            type_of_work=validated_data["type_of_work"],
            adhar_number=validated_data["adhar_number"],
            location=validated_data["location"],
            phone_number=validated_data["phone_number"],
            email=validated_data["email"],
            max_otp_try=settings.MAX_OTP_TRY,
            otp = otp,
            otp_expiry= otp_expiry
        )
        employee.save()
        if position_data:
            position_ids = [position.id if hasattr(position, 'id') else position for position in position_data]

            employee.position.set(position_ids)
        employee.set_password(validated_data["password1"])
        employee.save()
        username = validated_data["username"]
        email = validated_data["email"]
        subject = 'YOUR ACCOUNT VERIFICATION EMAIL'
        message = f'Your otp is{otp}'
        email_from = settings.EMAIL_HOST_USER
        context ={
            "username":username,
            "otp_message":message
        }
        html_messages = render_to_string("email.html",context=context)
        plain_message = strip_tags(html_messages)
        message = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=email_from,
            to=[email]
        )
        message.attach_alternative(html_messages,"text/html")
        message.send()
        return employee
