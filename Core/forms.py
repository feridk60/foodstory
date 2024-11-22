from django import forms
from .models import Contact,Subscriber

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fullname', 'email', 'subject', 'message']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }



class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']