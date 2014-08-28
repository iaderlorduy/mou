from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def sendMail(mail, asunto, mensaje):
	#return False
	send_mail(asunto,
	          mensaje,
	          '"mou.com.co" <info@mou.com.co>',
	          [mail])