from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import Subscriber

def send_email_to_subscribers(subject, context):
    
    email_list = Subscriber.objects.filter(is_active=True).values_list('email', flat=True)
    
    
    message = render_to_string('email-subscribers.html', context)
    
    
    mail = EmailMultiAlternatives(
        subject=subject,
        body=message,  
        from_email=settings.EMAIL_HOST_USER,
        to=email_list
    )
    
    
    mail.content_subtype = 'html'
    
    
    mail.send()
