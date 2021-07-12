from datetime import datetime
from django.core.mail import EmailMessage

def getHoursByIdentifier(identifier):
     createdTime = datetime.fromtimestamp(int(identifier)/1000)
     currentTime = datetime.now()
     diff = currentTime - createdTime
     days, seconds = diff.days, diff.seconds
     hours = days * 24 + seconds // 3600
     return hours

def sendEmailNotification(body):
     email = EmailMessage('Contribution Log', body, to=['samatvalive@gmail.com'])
     email.send()