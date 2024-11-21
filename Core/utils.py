from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import Subscriber

def send_email_to_subscribers(subject, context):
    # Aktif abonelerin e-posta adreslerini al
    email_list = Subscriber.objects.filter(is_active=True).values_list('email', flat=True)
    
    # E-posta içeriğini 'email-subscribers.html' şablonundan render et
    message = render_to_string('email-subscribers.html', context)
    
    # E-posta başlığını ve içeriğini ayarla
    mail = EmailMultiAlternatives(
        subject=subject,
        body=message,  # HTML içeriği
        from_email=settings.EMAIL_HOST_USER,
        to=email_list
    )
    
    # E-posta içeriği HTML olarak gönderilecek
    mail.content_subtype = 'html'
    
    # E-postayı gönder
    mail.send()
