from django.shortcuts import render
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
import json
import random
import string




class sendEmailAPI(APIView):
    def post(self, request):
        email = request.data.get("email",None)
        send_mail('subject', # 邮件标题
                  "message", # 邮件内容
                  settings.EMAIL_FROM, # 源
                  [email]) # 目的
        return Response({"msg":"邮件发送成功!"}, status=status.HTTP_200_OK)


